import threading
import dash
import dash_html_components as html
from dash import dcc, html, callback, Output, Input, State, no_update
from data_require import login_main,get_Data
from data_wash import data_main, swtich_download_data
from dash_tab import get_tab
from dash_graph import dash_slider_1,dash_graph_3,dash_slider_2
from datetime import datetime


def is_tradeing_time():
    # A股交易时间：9:30-11:30, 13:00-15:00
    market_open_morning_start = datetime.strptime("08:50", "%H:%M").time()
    market_open_morning_end = datetime.strptime("11:30", "%H:%M").time()
    market_open_afternoon_start = datetime.strptime("13:00", "%H:%M").time()
    market_open_afternoon_end = datetime.strptime("18:00", "%H:%M").time()
    current_time = datetime.now().time()
    if (market_open_morning_start <= current_time <= market_open_morning_end) or \
            (market_open_afternoon_start <= current_time <= market_open_afternoon_end):
        return True
    return False



def dashboard(data_dict):
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets,suppress_callback_exceptions=True)
    # 总体Tab设置
    app.layout = html.Div([
        ## header and logo
        html.Div([
            html.Br(),
            html.Img(
                src='cache_loader//420a987dc8c929c7263e625c56a087054610.jpeg',
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
                声明: 本网页内容仅限作品展示，其中数据皆随机生成，未经授权禁止转载或对外转发，否则后果自负，
                情节严重的将追究相应法律责任。
                '''),
            html.P("© Lorish Fo作品集")
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
        if is_tradeing_time():
            return dash_slider_1(data_dict,va)
        else:
            return no_update

    @app.callback(Output('historical_revenue','figure'),
                  [Input('slider-revenue-info','value')])
    def update_slider(va):
        if is_tradeing_time():
            return dash_slider_2(data_dict,va)
        else:
            return no_update


    @app.callback(Output('daily_revenue','figure'),
                  [Input('interval','n_intervals')])
    def update_minuts(n_interval):
        if is_tradeing_time():
            return dash_graph_3(data_dict)
        else:
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

    # 进入线程一、不断地更新数据到表格里面
    download_thread = threading.Thread(target=data_main,args=(cb,data_dict),daemon=True)
    download_thread.start()


    # 提取出数据进行画图就好了
    dashMain(dashboard(data_dict))
