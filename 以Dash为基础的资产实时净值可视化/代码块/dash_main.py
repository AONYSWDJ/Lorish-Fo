import threading
import time

import dash
import dash_html_components as html
from dash import dcc, html, callback, Output, Input, State, no_update
from data_require import login_main,get_Data,is_tradeing_time
from data_wash import data_main, swtich_download_data
from dash_tab import get_tab
from dash_graph import dash_slider_1,dash_graph_3,dash_slider_2
from datetime import datetime





def dashboard(data_dict):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)
    # 总体Tab设置
    app.layout = html.Div([
        ## header and logo
        html.Div([
            html.Br(),
            html.Img(
                src='https://i.loli.net/2020/11/16/Wg9bPV6xpCcQ8qy.png',
                style={
                    'height': '15%',
                    'width': '15%',
                    # 'float': 'right',
                    'position': 'relative',
                    'margin-top': 0,
                    'margin-left': 0,
                    # 'margin-right': 1600
                },
                className = 'two columns'
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.H1('Optimus Prime',className = 'ten columns', style = {'fontSize':25,'margin-top':0,'position':'relative',
                                                                        'margin-left':8, 'color': '#FF0000'}),
        ], className = 'row'),
        # Tab设置
        dcc.Tabs(id="tabs", value='tab-2', children=[
            dcc.Tab(label='产品净值和涨跌幅', value='tab-2')
            ],style={"font-size": "20px", "font-weight": "bold"},
                ),
        html.Div(id='tabs-content', className="tabs-content"),
        html.Div(className="div-note-bottom", children=[
            html.Br(),
            html.Br(),
            html.Hr(),
            html.P(
                '''
                声明: 本网页内容仅限公司内部员工使用，不构成任何投资建议，未经授权禁止转载或对外转发，否则按公司相关制度处罚，
                情节严重的将追究相应法律责任。
                '''),
            html.P("© 青岛安值投资管理有限公司")
        ]),
    ])


    @app.callback(Output('tabs-content', 'children'),
                  [Input('tabs', 'value')])
    def render_content(tab):
        if tab == 'tab-2':
            return get_tab(data_dict)


    @app.callback(Output('historical_dynamic','figure'),
                  [Input('slider-dynamic-info','value')])
    def update_slider(va):
        return dash_slider_1(data_dict,va)


    @app.callback(Output('historical_revenue','figure'),
                  [Input('slider-revenue-info','value')])
    def update_slider(va):

        return dash_slider_2(data_dict,va)



    @app.callback(Output('daily_revenue','figure'),
                  [Input('interval','n_intervals')])
    def update_minuts(n_interval):
        if is_tradeing_time():
            return dash_graph_3(data_dict)
        else:
            print('数据不更新')
            return no_update
    return app
def dashMain(app):
    app.run_server(debug=False, host='192.168.2.68', port=8050)
if __name__ == '__main__':

    # 定义全局字典，通过字典进行传参，目标是更新每一个key中的value值，然后读取参数即可
    data_dict ={}

    # 对字典进行第一次更新
    cb = login_main()
    data = get_Data(cb)
    swtich_download_data(data_dict,data)
    print('完成初始化更新')

    # 进入线程一、不断地更新数据到表格里面
    download_thread = threading.Thread(target=data_main,args=(cb,data_dict),daemon=True)
    download_thread.start()
    # 提取出数据进行画图就好了
    dashMain(dashboard(data_dict))
