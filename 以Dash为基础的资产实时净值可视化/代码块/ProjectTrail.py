from datetime import datetime
import dash
import datetime as dt

import numpy as np
import pandas as pd
from dash import dcc, html, callback, Output, Input, State, no_update
import plotly.graph_objects as go
import time
from pymssql import output
from win32con import PASSTHROUGH
import template_one
import demoforRequest
# 得到数据的 1.涨幅数据 2. 净资产 3每四秒更新的数值
#####
#### debug总是自己跳出去
####

'''

31号问题：
    首先，他有时候跑不出来就很迷，我怀疑是迅投自身老是自己出错重启这类的问题，因为它跑不出来的时候，迅投的数据也显示不出来
    第二个问题就是关于 interval的更新原理，好像有点不太对劲，和想要的结果 它总是会自己刷新，看是否可以改一下成局部刷新
    第三个问题是，在上午的时候，在不同文件夹的同名py竟然会出现调用出错的情况，本来是c盘的，选择open in file的时候，回会打开D盘的同名文件
                然后有个红色的感叹号出现。通过修改了命名后解决了这个问题
    第四个问题是关于gitee的，还是同名文件，一个叫做dash_developing，一个则是dash_show，然后还是会出现问题，dash_show竟然成了dash_developing的父文件夹
                            本来我为了解决问题三，另起炉灶在F盘创建了一个dash_show文件夹并连接到了gitee上。但是不知道为啥会出现这个问题。
                            对于gitee的操作真的还是一知半解。
13：50未完成功能：
    大体功能已经完成，需要补充的是y轴的单位显示，要不然就是平的线条
                    第二个需要解决的是x轴的显示，如果按照这样显示的话，x轴会看不清
                    第三个则是可能要解决的问题，也就是数据的存储，一天的数据每三秒更新的话，这个列表可能会很大，
                                            但具体应该怎么处理，没有个很好的方法，如果进行本地存储，然后15点删除，em，是个方法
                                                或者可以隔一段时间删掉一部分，但是这样，如果想看前面的怎么办？其实还是要有一个列表存储前面的值
                    第四个问题解决了，但是没想明白，dic_value作为一个可使数据，然后dic_value我只存储了一个列表，但是我list（dic——value）后，
                                    竟然出现了两个值，也就是list(dic_value)[0]和[1]，且二者相等，真奇怪，我怀疑是内部自己默认复制了一个防止报错

                    第五个需要解决的就是时间上，日常股市休市了，应该有一个时间上的判断，如果时间不在股市时间内，那就不进入interval循环
'''

'''
    哦吼，不适合放在一起，因为单位为0.0001，差距实在是太大了，适合放左右两个图 像subplot一样
    解决方式是双y轴法
'''

'''
问题和要求：
    三张图：历史净值，历史涨跌幅，实时净值
    功能完善：   
        画出rangdersldier，并且silder的起点的y轴要设置为1
            此时yesterday_value起到了扩充rangerslider的作用
        时间上的判断，如果时间不在股市开盘之内，则返回到上一个interval所对应的figure（内部仍然在循环，为了解放存储空间，这个时候可以删除list）
        interval计时器的选择，需要以主机的计时器作为基点，这样不会反复更新导致缓存出错，当然，也可以用status_restore进行更改
        细节的刻画，比如x轴和y轴的显示


愚人节项目进度： 全部完成！




                好吧，其实是
                愚人节快乐。
                完成了rangerslider的组件构成逻辑，并在第二张图上使用了组件，效果不错，但是需要一个时间判断func，预计今天可以完成
                那个涨跌幅需要改变的是yaxis的值，可以通过state value这一个参数进行回调，而且不是实时的，比较好做

                实时的rangerslider有点麻了，中间遇到了很多的strf与strp的时间判断问题，等下正好学以致用
                今天好像就上午学习如何用rangerslider，下午运用rangerslider。
                更改了一下第二幅图的表达形式，说实话，我倾向采用对数化，这样轨迹会比较明显，然后y轴的刻度就对应更改，好吧，也比较麻烦

                ok, 时间判断的func也完成了，现在如果是休盘时间，那么就no——update。
  File r"C:Users\Administrator\PycharmProjects\dashshow\dash_developing\Dash_second.py", line 257, in update_graph
    'range':[x_test_dt[slider_range[0]], x_test_dt[slider_range[1]]],  # 根据slider的值来更新x轴显示的时间范围
IndexError: list index out of range 时间判断上出现这样的报错

'''

'''
耗费了我半小时去思考这个问题，然后竟然被这样解决了，但是发生了什么嘛！！！！！！
figure本来是个字典就可以进行callback，然后突然graph-daily需要figure是一个列表，我就很迷啊，为什么之前都是字典，突然这个时候就要列表了呢？？？？？
然后全局变量被三个callback反复调用，直接乱跑，真是麻了麻了
'''

def is_trading_time(current_time):  # 加入时间判断，同时给自己的数据一个容错的时间
    # A股交易时间：9:30-11:30, 13:00-15:00
    market_open_morning_start = datetime.strptime("08:50", "%H:%M").time()
    market_open_morning_end = datetime.strptime("11:30", "%H:%M").time()
    market_open_afternoon_start = datetime.strptime("13:00", "%H:%M").time()
    market_open_afternoon_end = datetime.strptime("18:00", "%H:%M").time()
    current_time = current_time.time()
    if (market_open_morning_start <= current_time <= market_open_morning_end) or \
            (market_open_afternoon_start <= current_time <= market_open_afternoon_end):
        return True
    return False
"虽然有些麻烦，但是还是解决了，其实如果使用class的话，可以通过更新操作进行保存，但是事已至此，还是算了吧"
# 该套定义和方法转为daily graph使用
daily_interval_1 = {}
CV_test_1_1 = []
CV_test_1_2 = []
def get_data_1(cb):
    test1, test2, ticktime, yesterday_value = template_one.Conclusion(cb)


    test1 = test1[test1['净值'] != '-']
    test2 = test2[test2['净值'] != '-']

    test1['净值'] = test1['净值'].astype(float)
    test2['净值'] = test2['净值'].astype(float)

    X1_netValue = test1[['日期', '净值']]
    X1_timesValue = test1['净值'].iloc[0] / 100000000  # 以最后一个元素为1

    X2_netValue = test2[['日期', '净值']]
    X2_timesValue = test2['净值'].iloc[0] / 100000000  # 以最后一个元素为1

    X1_netValue = X1_netValue.sort_values(by='日期', ascending=True).reset_index(drop=True)
    X2_netValue = X2_netValue.sort_values(by='日期', ascending=True).reset_index(drop=True)

    if not CV_test_1_1:
        CV_test_1_1.append(yesterday_value[0] / 100000000)
        CV_test_1_2.append(yesterday_value[1] / 100000000)
        market_open_morning_start = datetime.strptime("08:50", "%H:%M").time().strftime('%H:%M:%S')
        daily_interval_1[market_open_morning_start] = [CV_test_1_1, CV_test_1_2]
    else:
        CV_test_1_1.append(X1_timesValue)
        CV_test_1_2.append(X2_timesValue)
        daily_interval_1[ticktime] = [CV_test_1_1, CV_test_1_2]

    return X1_netValue, X2_netValue, daily_interval_1

#该套为 historical-dynamic使用
daily_interval_2 = {}
CV_test_2_1 = []
CV_test_2_2 = []
def get_data_2(cb):
    test1, test2, ticktime, yesterday_value = template_one.Conclusion(cb)

    test1 = test1[test1['净值'] != '-']
    test2 = test2[test2['净值'] != '-']

    test1['净值'] = test1['净值'].astype(float)
    test2['净值'] = test2['净值'].astype(float)

    X1_netValue = test1[['日期', '净值']]
    X1_timesValue = test1['净值'].iloc[0] / 100000000  # 以最后一个元素为1

    X2_netValue = test2[['日期', '净值']]
    X2_timesValue = test2['净值'].iloc[0] / 100000000  # 以最后一个元素为1

    X1_netValue = X1_netValue.sort_values(by='日期', ascending=True).reset_index(drop=True)
    X2_netValue = X2_netValue.sort_values(by='日期', ascending=True).reset_index(drop=True)


    if not CV_test_2_1:
        CV_test_2_1.append(yesterday_value[0] / 100000000)
        CV_test_2_2.append(yesterday_value[1] / 100000000)
        market_open_morning_start = datetime.strptime("08:50", "%H:%M").time().strftime('%H:%M:%S')
        daily_interval_2[market_open_morning_start] = [CV_test_2_1, CV_test_2_2]
    else:
        CV_test_2_1.append(X1_timesValue)
        CV_test_2_2.append(X2_timesValue)
        daily_interval_2[ticktime] = [CV_test_2_1, CV_test_2_2]

    return X1_netValue, X2_netValue, daily_interval_2

# 该套为 historical使用
daily_interval_3 = {}
CV_test_3_1 = []
CV_test_3_2 = []
def get_data_3(cb):
    test1, test2, ticktime, yesterday_value = template_one.Conclusion(cb)


    test1 = test1[test1['净值'] != '-']
    test2 = test2[test2['净值'] != '-']

    test1['净值'] = test1['净值'].astype(float)
    test2['净值'] = test2['净值'].astype(float)

    X1_netValue = test1[['日期', '净值']]
    X1_timesValue = test1['净值'].iloc[0] / 100000000  # 以最后一个元素为1

    X2_netValue = test2[['日期', '净值']]
    X2_timesValue = test2['净值'].iloc[0] / 100000000  # 以最后一个元素为1

    X1_netValue = X1_netValue.sort_values(by='日期', ascending=True).reset_index(drop=True)
    X2_netValue = X2_netValue.sort_values(by='日期', ascending=True).reset_index(drop=True)


    if not CV_test_3_1:
        CV_test_3_1.append(yesterday_value[0] / 100000000)
        CV_test_3_2.append(yesterday_value[1] / 100000000)
        market_open_morning_start = datetime.strptime("08:50", "%H:%M").time().strftime('%H:%M:%S')
        daily_interval_3[market_open_morning_start] = [CV_test_3_1, CV_test_3_2]
    else:
        CV_test_3_1.append(X1_timesValue)
        CV_test_3_2.append(X2_timesValue)
        daily_interval_3[ticktime] = [CV_test_3_1, CV_test_3_2]

    return X1_netValue, X2_netValue, daily_interval_3



def dash_1(cb):
    app = dash.Dash(__name__)
    # 初始资产净值和时间
    # 用于记录每次更新的时间
    # 设置布局
    test1_stati = pd.read_csv('安值test1_history.csv')
    test1_static = test1_stati[test1_stati['净值'] != '-']
    test2_stati = pd.read_csv('安值test2_history.csv')
    test2_static = test2_stati[test2_stati['净值'] != '-']
    test_date = max(len(test1_static), len(test2_static))
    time_sequence_Df = test1_static.sort_values(by='日期', ascending=True).reset_index(drop=True)
    time_sequence = time_sequence_Df['日期']

    app.layout = html.Div([
        html.Div([
            html.H1('历史实时资产净值', style={'textAlign': 'left'}),
            html.Hr(style={"border": "3px solid black"}),
            dcc.Graph(id='net-worth-graph',
                        figure={
                        'data': [
                            go.Scatter(
                                x=test1_static['日期'],
                                y=test1_static['净值'],
                                mode='lines+markers',
                                name='资产净值test1',
                                line=dict(color='blue'),
                            ),
                            go.Scatter(
                                x=test2_static['日期'],
                                y=test2_static['净值'],
                                mode='lines+markers',
                                name='资产净值test2',
                                line=dict(color='red'),
                            )
                        ],
                        'layout': {
                            'title': '资产净值实时更新',
                            'xaxis': {'title': '时间', "fontsize": 20, 'showgrid': True, },
                            'yaxis': {'title': '资产净值', "fontsize": 20, 'showgrid': True},
                            'showlegend': True,
                            'height': 1000,
                            'width': 1200,
                            'hovermode': 'x+y'
                        }
                    }
                          ),
                dcc.RangeSlider(
                    id='slider-of-historical-dynamic',
                    min=0,
                    max=test_date,
                    step=15,
                    marks={i: f'{time_sequence[i]}' for i in range(0, test_date, 5)},  # 学习到了如何使用debug和console相结合的方法
                    value=[0, test_date-1]
                ),
                html.Button('切换到手动模式', id='manual-button-2', n_clicks=0)
            ]),
        html.Div([
            html.H1('当天实时资产净值', style={'textAlign': 'left'}),
            html.Hr(style={"border": "3px solid black"}),
            dcc.Graph(id='net-worth-daily'),
        html.Div([
            html.H1('历史资产涨跌幅', style={'textAlign': 'left'}),
            html.Hr(style={"border": "3px solid black"}),
            dcc.Graph(id='historical-netValue-of-Portfolio-test',
                      figure={
                          'data': [
                              go.Scatter(
                                  x=test1_static['日期'],
                                  y=test1_static['净值'],
                                  mode='lines+markers',
                                  name='资产净值test1',
                                  line=dict(color='blue'),
                              ),
                              go.Scatter(
                                  x=test2_static['日期'],
                                  y=test2_static['净值'],
                                  mode='lines+markers',
                                  name='资产净值test2',
                                  line=dict(color='red'),
                              )
                          ],
                          'layout': {
                              'title': '资产净值实时更新',
                              'xaxis': {'title': '时间', "fontsize": 20, 'showgrid': True, },
                              'yaxis': {'title': '资产净值', "fontsize": 20, 'showgrid': True},
                              'showlegend': True,
                              'height': 1000,
                              'width': 1200,
                              'hovermode': 'x+y'
                          }
                      }
                      ),
        ]
                      ),
            dcc.RangeSlider(
                id='slider-of-historical',
                min=0,
                max=test_date,
                step=15,
                marks={i: f'{time_sequence[i]}' for i in range(0, test_date, 5)},
                value=[0, test_date-1]
            ),
            html.Button('切换到手动模式', id='manual-button-3', n_clicks=0)
        ]),
        dcc.Interval(
            id='interval-update',
            interval=60000,  # 每 60000 毫秒（60秒）更新一次
            n_intervals=0,  # 初始时，计数为0
        )
    ])
    # 定义回调函数1，对当天实时净值进行callback 之前最难的变成了现在最简单的了hh
    @ app.callback([
        Output('net-worth-daily', 'figure'),
    ],
        [
            Input('interval-update', 'n_intervals'),
        ]
    )
    def update_graph(n_intervals):

        X1_netValue, X2_netValue, daily_time_dic = get_data_1(cb)
        x_test = list(daily_time_dic.keys())
        x_test_dt = [datetime.strptime(i, '%H:%M:%S') for i in x_test]

        current_time = x_test_dt[-1]

        if not is_trading_time(current_time):  # 如果在休盘，那么就保持原样
            return [dash.no_update]
        else:
            test1_ = np.array(list(daily_time_dic.values())[0][0])
            test2_ = np.array(list(daily_time_dic.values())[0][1])


            test1__ = test1_[1:]/test1_[:-1]
            ratio_1 = np.insert(test1__,0,1)
            test2__ = test2_[1:]/test2_[:-1]
            ratio_2 = np.insert(test2__, 0, 1)

            ratio__1 = np.cumprod(ratio_1)
            ratio__2 = np.cumprod(ratio_2)

            #
            figure2 = [{
                'data': [
                    go.Scatter(
                        x=x_test,
                        y=ratio__1,
                        mode='lines+markers',
                        name='资产净值test1',
                        line=dict(color='blue'),

                    ),
                    go.Scatter(
                        x=list(daily_time_dic.keys()),
                        y=ratio__2,
                        mode='lines+markers',
                        name='资产净值test2',
                        line=dict(color='red'),

                    )
                ],
                'layout': {
                    'title': '当天资产净值实时更新',
                    'xaxis': {'title': '时间', "fontsize": 20, 'showgrid': True, 'rangeslider': True},
                    'yaxis': {'title': '资产净值', "fontsize": 20, 'showgrid': True},
                    'showlegend': True,
                    'height': 1000,
                    'width': 1200,
                    'hovermode': 'x+y'
                }
            }]

        return figure2
    # 定义回调函数2， 对历史实时净值进行callback
    @app.callback([
        Output('net-worth-graph', 'figure'),
        Output('slider-of-historical-dynamic', 'value'),
        Output('manual-button-2', 'n_clicks'),
    ],
        [
            Input('interval-update', 'n_intervals'),
            Input('slider-of-historical-dynamic', 'value'),
            Input('manual-button-2', 'n_clicks'),

        ],
        [State('slider-of-historical-dynamic', 'value')]
    )
    def update_chart2(n_intervals, slider_range, manual_clicks, current_slider_value):

        X1_netValue, X2_netValue, daily_time_dic = get_data_2(cb)


        x_test = list(daily_time_dic.keys())
        x_test_dt = [datetime.strptime(i, '%H:%M:%S') for i in x_test]
        current_time = x_test_dt[-1]
        if not is_trading_time(current_time):  # 如果在休盘，那么就保持原样
            return [dash.no_update] * 3
        else:
            figure1 = {
                'data': [
                    go.Scatter(
                        x=X1_netValue['日期'],
                        y=X1_netValue['净值'],
                        mode='lines+markers',
                        name='资产净值test1',
                        line=dict(color='blue'),
                    ),
                    go.Scatter(
                        x=X2_netValue['日期'],
                        y=X2_netValue['净值'],
                        mode='lines+markers',
                        name='资产净值test2',
                        line=dict(color='red'),
                    )
                ],
                'layout': {
                    'title': '资产净值实时更新',
                    'xaxis': {'title': '时间', "fontsize": 20, 'showgrid': True,'range':[X1_netValue['日期'][slider_range[0]],X1_netValue['日期'][slider_range[1]]]},
                    'yaxis': {'title': '资产净值', "fontsize": 20, 'showgrid': True,},
                    'showlegend': True,
                    'height': 1000,
                    'width': 1200,
                    'hovermode': 'x+y'
                }
            }

            if int(manual_clicks + 1) % int(2) == 0:
                value = current_slider_value  # 保持手动选择的范围
                return figure1, value, manual_clicks
            elif int(manual_clicks + 1) % 2 == 1:
                # 自动更新slider的值到最大值
                value = [slider_range[0], test_date-1]  # 自动显示最新的数据
                return figure1, value, manual_clicks

    # 回调函数3，对涨跌幅进行的callback
    @app.callback([
        Output('historical-netValue-of-Portfolio-test', 'figure'),
        Output('slider-of-historical', 'value'),
        Output('manual-button-3', 'n_clicks'),
    ],
        [
            Input('interval-update', 'n_intervals'),
            Input('slider-of-historical', 'value'),
            Input('manual-button-3', 'n_clicks'),

        ],
        [State('slider-of-historical', 'value')]
    )
    def update_chart3(n_intervals, slider_range, manual_clicks, current_slider_value):

        X1_netValue, X2_netValue, daily_time_dic = get_data_3(cb)

        x_test = list(daily_time_dic.keys())
        x_test_dt = [datetime.strptime(i, '%H:%M:%S') for i in x_test]
        current_time = x_test_dt[-1]
        if not is_trading_time(current_time):  # 如果在休盘，那么就保持原样
            return [dash.no_update] * 2
        else:
            elements_1 = X1_netValue['净值'] / X1_netValue['净值'][current_slider_value[0]]
            elements_1['累计涨跌幅'] = elements_1.cumprod()-1
            elements_2 = X2_netValue['净值'] / X2_netValue['净值'][current_slider_value[0]]
            elements_2['累计涨跌幅'] = elements_2.cumprod()-1

            figure1 = {
                'data': [
                    go.Scatter(
                        x=X1_netValue['日期'],
                        y=elements_1['累计涨跌幅'],
                        mode='lines+markers',
                        name='资产净值test1',
                        line=dict(color='blue'),
                    ),
                    go.Scatter(
                        x=X2_netValue['日期'],
                        y=elements_2['累计涨跌幅'],
                        mode='lines+markers',
                        name='资产净值test2',
                        line=dict(color='red'),
                    )
                ],
                'layout': {
                    'title': '资产净值实时更新',
                    'xaxis': {'title': '时间', "fontsize": 20, 'showgrid': True, 'range':[X1_netValue['日期'][slider_range[0]],X1_netValue['日期'][slider_range[1]]]},
                    'yaxis': {'title': '资产净值', "fontsize": 20, 'showgrid': True,'range':[0.7-2.8]},
                    'showlegend': True,
                    'height': 1000,
                    'width': 1200,
                    'hovermode': 'x+y'
                }
            }

            if int(manual_clicks + 1) % int(2) == 0:
                value = current_slider_value  # 保持手动选择的范围
                return figure1, value, manual_clicks
            elif int(manual_clicks + 1) % 2 == 1:
                # 自动更新slider的值到最大值
                value = [slider_range[0], test_date-1]  # 自动显示最新的数据
                return figure1, value, manual_clicks

    return app


if __name__ == "__main__":
    server_addr = "175.25.41.106:65300 "  # 统一交易服务器的地址
    username = "安值_独立交易员"  # 测试用户，同客户端登录用户，非资金账号
    password = "(输入自己代码)"  # 用户密码，客户端登录密码，非资金密码
    cb = demoforRequest.CallBack(server_addr, username, password)
    cb.init()
    cb.join()
    time.sleep(3)
    app = dash_1(cb)
    app.run_server(debug=False, host='192.168.2.68', port=8050)
