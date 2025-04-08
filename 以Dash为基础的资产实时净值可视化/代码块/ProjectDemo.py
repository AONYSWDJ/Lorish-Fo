# Dashapi将以多个函数的形式满足所有的功能需求,在数据获取和数据保存方面单开一个线程，实时保存
# 而dash画图可以作为主线程，等待子线程dowload_data后，用interval进行调用并绘图
import os.path
# 如何满足接口化？以列表的形式传入参数
# 获取产品名字，然后对应到下载 产品名_history.csv 的文件 同时每日的数据进行更新 并且下载，这一步维护方便
#                         主要是这一步需要人工判断，也就是自行下载，然后再每日更新的对应
import time
import threading
import queue
from datetime import datetime
import dash
import datetime as dt
import pandas as pd
import numpy as np
from dash import dcc, html, callback, Output, Input, State, no_update
from scipy.optimize import newton
import plotly.graph_objects as go
import demoforRequest
from threading import Lock
##### 全局变量函数
callback_times = 0 # callback中，interval的次数，

cached_dict = {} # 除去第一个callback函数，其他的callback函数通过全局字典的最新值进行访问
dict_lock = threading.Lock()
#####
def login_main():
    server_addr = "175.25.41.106:65300"  # 统一交易服务器的地址
    username = "安值_独立交易员"  # 测试用户，同客户端登录用户，非资金账号
    password = "az913702"  # 用户密码，客户端登录密码，非资金密码
    cb = demoforRequest.CallBack(server_addr, username, password)
    cb.init()
    cb.join()
    time.sleep(3)
    return cb
def get_Data(cb):
    #第一步，得到目前的时间，然后后续按照要求进行分割即可
    current_time = dt.datetime.now()
    productlist = cb.reqProductDataSync()
    product_name_list, product_net_value_list, product_yesterday_value_list = [], [], []
    #第二步，得到产品名字列表，然后依据产品列表的长度，进行数据集合的创建
    for data in productlist:
        product_name = data.m_strProductName
        product_name_list.append(product_name)

        product_net_value = data.m_dTotalNetValue
        product_net_value_list.append(product_net_value)

        product_yesterday_value = data.m_dPrevTotalNetValue
        product_yesterday_value_list.append(product_yesterday_value)

    return [product_name_list,product_net_value_list,product_yesterday_value_list,current_time]
def daily_down_data(curren_time,product_names,product_netValue,i):
        # 应该进行增量更新，保证只有一个读取和写入，这样的情况下，就不容易犯下错误
        # 那么此时写入的时候就应该调换时间
    current_time = curren_time.strftime('%H:%M:%S')
    initial_df = pd.read_csv(fr'cache_loader\{product_names[i]}_daily.csv')

    new_df = pd.DataFrame({
        '产品名': f'{product_names[i]}',
        '时间': [current_time],
        "净值": [product_netValue[i]]
    })
    df_product = pd.concat([initial_df, new_df], axis=0, ignore_index=True)
    df_product = df_product.sort_values(by='时间', ascending=True).reset_index(drop=True)
    df_product.to_csv(fr'cache_loader\{product_names[i]}_daily.csv', index=False)
        # 在这一步中，保存了新的时间，对本地文件进行了更新，然后出传出了df_product

    return df_product
def swtich_download_data(n,data): # 进行格式上的转换，包括日期，涨跌幅，
    # 以产品名字作为判断标准
    # 对每一个数据进行取值
    # 创建一个dataframe，其中保留地址，这一个步骤在目前的程序中只能手动做到了
    '''
    ######## 下载到本地，然后按照名字依次取名，历史数据记得取名字 productName_history.csv#####
    ####### 当日数据则保存为 productName_daily.csv #########
    '''
    product_amounts = len(data[0])
    product_names = data[0]
    product_netValue = data[1]
    product_yesterdayValue = data[2]
    product_currentTime = data[3]
    # 这样设置健壮性总是比直接设置要好点，越来越科班了hh
    historical_list, daily_list = [],[]
    # #创建需要读取的文件地址，这样上传到队列中，就相当于True的作用了,这样可能会阻塞并且耽误时间，所以用增量更新方法
    # local__history_address = []
    # local__daily_address = []
    #### 增量更新就是只在生产者线程中进行数据的更新和保存，然后消费者直接拿到数据进行消费即可，不需要本地读取数据，这样
    #### 这样就可以保证文件的单独访问而不会在系统的线程中串行


    for i in range(0,product_amounts): # 录入-修改-保存
        # 读取产品最初保存在本地的地址
        product_df = pd.read_csv(fr'cache_loader\{product_names[i]}_history.csv',encoding='UTF-8')
    # 对日期进行更新，其实第一步是不太需要的，但还是直接copy上去吧
        product_df['产品名'] = product_names[i]
        product_df['日期'] = pd.to_datetime(product_df['日期'].astype(str))
        pd.set_option('mode.chained_assignment',None) # 忽略报错信息
        #开始判断时间
        daytime = product_currentTime.date()
        if product_df['日期'].iloc[0] == daytime:
            product_df['净值'].iloc[0] = product_netValue[i]
            df_product = product_df
            df_product.to_csv(fr'cache_loader\{product_names[i]}_history.csv',index=False)
        # 忘记了，除了周末还有节假日，这样的话干脆直接进行判断当天和非当天
        # 如果是非当天的话，那么就按照

        # 这一步还需要调节维护的点在于，如果工作日隔了两天没有运作，那么最好重置cache_loader
        else:
            new_df = pd.DataFrame({
                '产品名': f'{product_names[i]}',
                '日期': daytime,
                "净值": [float(product_netValue[i])]
            })
            df_product = pd.concat([product_df,new_df],axis=0,ignore_index=True)
            df_product = df_product.sort_values(by='日期', ascending=False).reset_index(drop=True)
            df_product.to_csv(fr'cache_loader\{product_names[i]}_history.csv',index=False)
        historical_list.append(df_product)
        # 保存数据到本地后，进行预处理上传列表
        # 开始增量更新模式
        # 起初最开始需要一次判断，如果存在这个文件，就不需要重新创建
        if os.path.exists(fr'cache_loader\{product_names[i]}_daily.csv'):
            daily_df = daily_down_data(product_currentTime, product_names, product_netValue, i)
            daily_list.append(daily_df)
        else:
            initial_df = pd.DataFrame({
                '产品名': f'{product_names[i]}',
                '时间': datetime.strptime('8:50:00','%H:%M:%S').time(),
                "净值": [product_yesterdayValue[i]]
            })
            initial_df.to_csv(fr'cache_loader\{product_names[i]}_daily.csv',index=False)
            daily_df = daily_down_data(product_currentTime,product_names,product_netValue,i)
            daily_list.append(daily_df)

    # 对地址进行一个线程上传
    with dict_lock:
        cached_dict[f'第{n}次更新数据'] = [historical_list, daily_list]
def download_main(cb):
    n = 1
    while True:
        #持续调用 获取函数、整理函数、下载函数、当执行完成时，dash线程才开始执行
        #由于为了每天都能显示到数据，这个时候就需要指定dash阅读本地数据，所以data_queue可以传入文件名
        data = get_Data(cb)
        swtich_download_data(n,data)
        n += 1
        print('数据已更新到本地')
        time.sleep(1)

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
def amends_initial_data(historical_dfs): # 用来调整dash中导入的数据的,保证初始化的绘图没有问题
    initial_xy = []
    revenue_xy = []
    # 得到普通的数据，然后ascending顺序排列
    # 得到涨跌幅的数据
    for address in historical_dfs:
        historical_d = address #这个算是接口时候给我记一下我更新的错误吧，烦死了烦死了啊啊啊啊啊啊啊
        historical_df = historical_d[historical_d['净值'] != '-']
        historical_Df = historical_df.sort_values(by='日期', ascending=True).reset_index(drop=True)
        # 开始得到涨跌幅的数据
        initial_xy.append(historical_Df)
        historical_Df['涨跌幅'] = (historical_Df['净值'].astype(float)/ historical_Df['净值'].astype(float).shift(1)).fillna(1)
        historical_Df['累计涨跌幅'] = historical_Df['涨跌幅'].cumprod() -1

        revenue_xy.append(historical_Df)
    return [initial_xy,revenue_xy]
def amends_refresh_data(daily_dfs): # 用来调整数据的时间格式，顺序等其他问题，保证后续callback能正常调用
    revenue_xy = []
    for address in daily_dfs:
        # 开始得到涨跌幅的数据
        address['净值'] = address['净值'].replace('-',np.nan).ffill().bfill()
        address['涨跌幅'] = (address['净值'].astype(float) / address['净值'].astype(float).shift(1)).fillna(1)
        address['累计涨跌幅'] = address['涨跌幅'].cumprod() - 1
        revenue_xy.append(address)

    return revenue_xy #还是同理，获得了一个列表，列表包含了所有产品的涨跌幅
def rangeslider_draw(initial_xy):
    sliders_max = 0
    slider_date = None
    for i,xy in enumerate(initial_xy):
        # 开始得到最大的max，将其作为slider的长度
        slider_max = len(xy['日期'])
        if slider_max >= sliders_max:
            sliders_max = slider_max
            slider_date = xy['日期'].dt.date
        else:
            continue
    return sliders_max, slider_date
def initial_graph(data_xy):
    #载入数据
    #首先是要确定到底要话多少条线，那么就对应配套的go.scatter
    # 由于里面的data_key对应的是个列表，所以传入一个列表即可

    colors = ['blue', 'red', 'green', 'orange', 'purple']
    initial_xy = data_xy[0] # 第一个初始scatter
    data_set_1 = [] # 第一个初始的data

#### 第二个没有初始化data，所以不设置#####

    revenue_xy = data_xy[1] # 第三个初始scatter
    data_set_3 = [] # 第三个初始的data

    #关于slider 和其需要的日期排序
    sliders_max,slider_date = rangeslider_draw(initial_xy)


    for i,xy in enumerate(initial_xy):
        # 传入data
        product_name = xy['产品名'].iloc[0]
        Historical_Net_Traces = go.Scatter(
                x=xy['日期'],
            y=xy['净值'],
            mode='lines+markers',
            name=f"{product_name}历史净值曲线",
            line=dict(color=colors[i % len(colors)],width=2),
        )
        data_set_1.append(Historical_Net_Traces)
    for i,xy in enumerate(revenue_xy):
        product_name = xy['产品名'].iloc[0]
        Revenue_Traces = go.Scatter(
            x=xy['日期'],
            y=xy['累计涨跌幅'],
            mode='lines+markers',
            name=f'{product_name}历史涨跌幅曲线',
            line=dict(color=colors[i % len(colors)], width=2),
        )
        data_set_3.append(Revenue_Traces)
    # 涨跌幅

    layout = html.Div([
        html.Div([
            html.H1('历史实时资产净值', style={'textAlign': 'left'}),
            html.Hr(style={"border": "3px solid black"}),
            dcc.Graph(id='net-worth-graph',
                        figure={
                        'data': data_set_1,
                        'layout': {
                            'title': '产品资产净值实时更新',
                            'xaxis': {'title': '日期', "fontsize": 20, 'showgrid': True, },
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
                    max=sliders_max,
                    step=5,
                    marks={i: f'{slider_date[i]}' for i in range(0, sliders_max,5)},  # 学习到了如何使用debug和console相结合的方法
                    value=[0, sliders_max-1]
                ),
                html.Button('更新到最新日期', id='manual-button-1', n_clicks=0)
            ]),
        html.Div([
            html.H1('当天实时资产净值', style={'textAlign': 'left'}),
            html.Hr(style={"border": "3px solid black"}),
            dcc.Graph(id='net-worth-daily')]),
        html.Div([
            html.H1('历史资产涨跌幅', style={'textAlign': 'left'}),
            html.Hr(style={"border": "3px solid black"}),
            dcc.Graph(id='historical-netValue-of-Portfolio-test',
                      figure={
                          'data': data_set_3,
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
                id='slider-of-historical',
                min=0,
                max=sliders_max,
                step=5,
                marks={i: f'{slider_date[i]}' for i in range(0, sliders_max, 5)},
                value=[0, sliders_max-1]
            ),
            html.Button('更新到最新日期', id='manual-button-3', n_clicks=0)
        ]),
        dcc.Interval(
            id='interval-update',
            interval=10000,  # 每 60000 毫秒（60秒）更新一次
            n_intervals=0,  # 初始时，计数为0
        ),
        dcc.Store(id='stored_interval',storage_type='local')
    ])
    return layout
def scatter_graph(df,time,column,i,*args):
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    if args:
        current_slider_value = args[0]
        y = df[column][current_slider_value[0]]
    else:
        y = df[column]

    scatter = go.Scatter(
        x = df[time],
        y = y,
        mode='lines+markers',
        name=f'{df["产品名"][0]}历史净值曲线',
        line=dict(color=colors[i % len(colors)], width=2,shape='spline'),
    )
    return scatter
def initial_get_data(cb):
    # 主线程中，首先初始化获得所有数据，然后导入到dash主线程中。
    data = get_Data(cb)
    product_amounts = len(data[0])
    product_names = data[0]
    product_netValue = data[1]
    product_yesterdayValue = data[2]
    product_currentTime = data[3]
    # 这样设置健壮性总是比直接设置要好点，越来越科班了hh
    historical_list, daily_list = [], []
    # #创建需要读取的文件地址，这样上传到队列中，就相当于True的作用了,这样可能会阻塞并且耽误时间，所以用增量更新方法
    # local__history_address = []
    # local__daily_address = []
    #### 增量更新就是只在生产者线程中进行数据的更新和保存，然后消费者直接拿到数据进行消费即可，不需要本地读取数据，这样
    #### 这样就可以保证文件的单独访问而不会在系统的线程中串行
    for i in range(0, product_amounts):  # 录入-修改-保存
        # 读取产品最初保存在本地的地址
        product_df = pd.read_csv(fr'cache_loader\{product_names[i]}_history.csv', encoding='UTF-8')
        # 对日期进行更新，其实第一步是不太需要的，但还是直接copy上去吧
        product_df['产品名'] = product_names[i]
        product_df['日期'] = pd.to_datetime(product_df['日期'].astype(str))
        pd.set_option('mode.chained_assignment', None)  # 忽略报错信息
        # 开始判断时间
        daytime = product_currentTime.date()
        if product_df['日期'].iloc[0] == daytime:
            product_df['净值'].iloc[0] = product_netValue[i]
            df_product = product_df

        else:
            new_df = pd.DataFrame({
                '产品名': f'{product_names[i]}',
                '日期': daytime,
                "净值": [float(product_netValue[i])]
            })
            df_product = pd.concat([product_df, new_df], axis=0, ignore_index=True)
            df_product = df_product.sort_values(by='日期', ascending=False).reset_index(drop=True)
        historical_list.append(df_product)
        # 保存数据到本地后，进行预处理上传列表
        # 开始增量更新模式
    return [historical_list,daily_list]
def dashing(data_initial): #当子线程执行完后一次后，立马获得数据，
    app = dash.Dash()
    #在子线程中，反正初始化的时候在直接使用get_data，然后开始画图
    historical_daily = data_initial
    # 得到一个储存了历史净资产的数据
    historical = historical_daily[0]
    xy = amends_initial_data(historical)
    # 开始外包画图func
    app.layout = initial_graph(xy)

    ###### ok 在我的理解中，上述步骤逻辑是行得通的


    # 回调函数零： 保存此时的interval的值
    @app.callback(
        Output('interval-store', 'data'),
        [Input('interval-component', 'n_intervals')],
        [State('interval-store', 'data')]
    )
    def update_store(n,d):
        if d == None:
            d = 1
        else:
            d += 1
        return d

    # 回调函数1： 对当天的实时净值进行callback，并且是用增长幅度进行
    @app.callback([
        Output('net-worth-daily', 'figure'),
        Output('stored-interval', 'data'),
    ],[
            Input('interval-update', 'n_intervals'),
        ],
        [State('stored_interval','data')]
    )
    def up_graph(n_intervals,data):
        if data == None:
            data = 1
        else:
            with dict_lock:
                df_list = cached_dict.get(f'第{data}次更新数据')
        if df_list is None:
            print('此时字典为空')
            return [dash.no_update] * 2
        df_daily = df_list[1] # 获取到当天数据的列表
        #第一步进行时间上的判断，如果是休盘时间，那么就不更新
        currentTime = df_daily[0]['时间'].iloc[-1]
        current_times = datetime.strptime(currentTime,'%H:%M:%S')
        if not is_trading_time(current_times):
            return [dash.no_update]*2
        else:
            traces = []
            dfs_day = amends_refresh_data(df_daily) # 获取此时的数据并且修正为涨跌幅
            for i,df_day in enumerate(dfs_day):
                revenue_traces = scatter_graph(df_day,'时间','累计涨跌幅',i)
                traces.append(revenue_traces)
            figure = [
                {
                'data':traces,
                'layout':
                    {
                    'title': '当天资产净值实时更新',
                    'xaxis': {'title': '时间', "fontsize": 20, 'showgrid': True,'dtick':7,'rangeslider': True},
                    'yaxis': {'title': '资产净值', "fontsize": 20, 'showgrid': True},
                    'showlegend': True,
                    'height': 1000,
                    'width': 1200,
                    'hovermode': 'x+y'
                    }
                }]




        return figure, data

    #回调函数2： 对历史实时净值进行callback，此时记得调用的是字典里面的数值进行更新
    @app.callback([
        Output('net-worth-graph', 'figure'),
        Output('slider-of-historical-dynamic', 'value'),
        Output('manual-button-1', 'n_clicks'),
        Output('manual-button-1', 'children'),
        Output('stored_interval', 'data')

    ],
        [
            Input('interval-update', 'n_intervals'),
            Input('slider-of-historical-dynamic', 'value'),
            Input('manual-button-1', 'n_clicks'),
        ],
        [State('slider-of-historical-dynamic', 'value'),
         State('stored_interval','data')
         ]
    )
    def up_graph2(n_interval,slider_range, manual_clicks, current_slider_value, data):
        if data == None:
            data = 1
        else:
            with dict_lock:
                historical_df = cached_dict.get(f'第{data}次更新数据')
        if historical_df is None:
            print('此时字典为空')
            return [dash.no_update]*6
        print(f'成功读取全局变量字典，第{data}次绘制')
        # historical_df = data_queue.get()
        historical_dfs = historical_df[0]
        currentTime = historical_df[1][0]['时间'].iloc[-1]
        current_times = datetime.strptime(currentTime,'%H:%M:%S')
        if not is_trading_time(current_times):
            return [dash.no_update]*5
        else:
            #修改dfs的格式，删除空值以及增加累计涨跌幅
            historical_dfss = amends_initial_data(historical_dfs)[0]



            empty,test_date = rangeslider_draw(historical_dfss)
            traces = []
            for i,historical_df in enumerate(historical_dfs):
                historical_track = scatter_graph(historical_df,'日期','净值',i)
                traces.append(historical_track)
            figure = [
                {
                'data':traces,
                'layout':
                    {
                    'title': '历史资产净值实时更新',
                    'xaxis': {'title': '时间', "fontsize": 20, 'showgrid': True,'dtick':7, 'range':[test_date[slider_range[0]],test_date[slider_range[1]]]},
                    'yaxis': {'title': '资产净值', "fontsize": 20, 'showgrid': True},
                    'showlegend': True,
                    'height': 1000,
                    'width': 1200,
                    'hovermode': 'x+y'
                    }
                }]

            if int(manual_clicks + 1) % int(2) == 0:
                value = [slider_range[0], empty - 1]  # 自动显示最新的数据
                children= '点击手动拉取范围'
                return figure, value, manual_clicks,children,data

            elif int(manual_clicks + 1) % 2 == 1:
                # 自动更新slider的值到最大值
                value = current_slider_value  # 保持手动选择的范围
                children = '点击自动更新到最大值'

                return figure, value, manual_clicks,children,data
    @app.callback([
        Output('historical-netValue-of-Portfolio-test', 'figure'),
        Output('slider-of-historical', 'value'),
        Output('manual-button-3', 'n_clicks'),
        Output('manual-button-3', 'children'),
        Output('stored_interval', 'data')

    ],
        [
            Input('interval-update', 'n_intervals'),
            Input('slider-of-historical-dynamic', 'value'),
            Input('manual-button-3', 'n_clicks'),


        ],
        [State('slider-of-historical', 'value'),
         State('stored_interval', 'data')
         ]
    )
    ###  对于债的更新
    def up_graph3(n_interval, slider_range, manual_clicks, current_slider_value,data):
        if data == None:
            data = 1
        else:
            with dict_lock:
                historical_df = cached_dict.get(f'第{data}次更新数据')
        if historical_df is None:
            print('此时字典为空')
            return [dash.no_update] * 5
        print(f'成功读取全局变量字典，第{data}次绘制图形')
        # historical_df = data_queue.get()
        historical_dfs = historical_df[0]
        currentTime = historical_df[1][0]['时间'].iloc[-1]
        current_times = datetime.strptime(currentTime,'%H:%M:%S')
        if not is_trading_time(current_times):
            print('休盘中')
            return [dash.no_update]*5
        else:
            historical_dfs = amends_initial_data(historical_dfs)[1]
            empty,test_date = rangeslider_draw(historical_dfs)
            traces = []
            revenue_df = amends_refresh_data(historical_dfs)
            for i, historical_df in enumerate(revenue_df):
                historical_track = scatter_graph(historical_df, '日期', '累计涨跌幅', i,current_slider_value)
                traces.append(historical_track)
            figure = [
                {
                    'data': traces,
                    'layout':
                        {
                            'title': '历史累计涨跌幅实时更新',
                            'xaxis': {'title': '时间', "fontsize": 20, 'showgrid': True,'dtick':7, 'range':[test_date[slider_range[0]],test_date[slider_range[1]]]},
                            'yaxis': {'title': '资产净值', "fontsize": 20, 'showgrid': True},
                            'showlegend': True,
                            'height': 1000,
                            'width': 1200,
                            'hovermode': 'x+y'
                        }
                }]

            if int(manual_clicks + 1) % int(2) == 0:
                value = current_slider_value  # 保持手动选择的范围
                children = '点击自动更新到最大值'
                return figure, value, manual_clicks, children,data
            elif int(manual_clicks + 1) % 2 == 1:
                # 自动更新slider的值到最大值
                value = [slider_range[0], empty - 1]  # 自动显示最新的数据
                children = '点击手动拉取范围'
                return figure, value, manual_clicks, children,data
    return app
def dashing_main(cb): #专门用来画图
    app = dashing(cb)
    app.run_server(debug=False, host='192.168.2.68', port=8050)

def main():
    cb = login_main() # 作为主线程
    data_initial = initial_get_data(cb)
    #创建下载数据的线程
    download_Thread = threading.Thread(target=download_main, args=(cb,), daemon=True)
    download_Thread.start()
    #创建绘图的线程
    dashing_Thread = threading.Thread(target=dashing_main, args=(data_initial,), daemon=True)
    dashing_Thread.start()

    while True:
        time.sleep(1)

if __name__ == '__main__':
    main()