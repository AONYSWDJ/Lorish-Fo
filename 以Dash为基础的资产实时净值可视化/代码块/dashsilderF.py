import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
from datetime import datetime, timedelta
import plotly.graph_objs as go
import random

# 创建 Dash 应用
app = dash.Dash(__name__)

# 初始时间设置

# 模拟折线图数据（模拟实时更新）
x_data = []
y_data = []

# 应用布局
app.layout = html.Div([
    html.H1("动态更新的 RangeSlider 和折线图示例"),

    # 折线图组件
    dcc.Graph(id='line-graph'),

    # RangeSlider 组件
    dcc.RangeSlider(
        id='time-range-slider',
        min=0,  # 起始时间对应的数字
        max=0,  # 这个会通过回调动态更新
        step=1,  # 每次增加1分钟
        marks={},  # 初始时刻度为空，后面会动态生成
        value=[0, 0],  # 默认选择的时间范围，初始化后会动态设置
    ),

    # 刷新按钮
    html.Button('切换到手动模式', id='manual-button', n_clicks=0),

    # 显示当前的最大时间
    html.Div(id='slider-output-container'),

    # 定时更新组件，每2秒更新一次
    dcc.Interval(
        id='interval-component',
        interval=2000,  # 每2000毫秒（即2秒）更新一次
        n_intervals=0  # 初始为0次
    ),
])

# 更新折线图和slider的最大时间，并显示
@app.callback(
    [Output('line-graph', 'figure'),
     Output('time-range-slider', 'max'),
     Output('time-range-slider', 'marks'),
     Output('slider-output-container', 'children'),
     Output('time-range-slider', 'value'),
     Output('manual-button', 'n_clicks')],
    [Input('interval-component', 'n_intervals'),
     Input('time-range-slider', 'value'),
     Input('manual-button', 'n_clicks')],
    [State('time-range-slider', 'value')]  # 当前的slider值，用来切换模式
)
def update_graph_and_slider(n_intervals, slider_range, manual_clicks, current_slider_value):
    # 生成新的时间点，每次增加一分钟
    start_time = datetime.strptime("9:50", "%H:%M")
    current_time = start_time + timedelta(minutes=n_intervals)

    # 模拟折线图数据（你可以根据实际情况替换）
    x_data.append(current_time)
    y_data.append(random.randint(100, 200))  # 模拟数据

    # 创建折线图
    figure = {
        'data': [
            go.Scatter(
                x=x_data,
                y=y_data,
                mode='lines+markers',
                name='实时数据',
                line=dict(color='blue'),
            ),
        ],
        'layout': {
            'title': '实时折线图',
            'xaxis': {
                'title': '时间',
                'tickformat': '%H:%M',  # 每分钟为单位
                'range': [x_data[slider_range[0]], x_data[slider_range[1]]],  # 根据slider的值来更新x轴显示的时间范围
            },
            'yaxis': {
                'title': '值',
            },
        },
    }

    # 获取当前最大时间（单位：分钟）
    max_time = current_time
    max_minutes = int((max_time - start_time).total_seconds() / 60)

    # 动态生成marks，每小时一个标记
    marks = {}
    for i in range(0, max_minutes + 1, 5):
        mark_time = start_time + timedelta(minutes=i)
        marks[i] = mark_time.strftime("%H:%M")

    # 如果点击了切换到手动模式按钮，进入手动模式
    if manual_clicks%int(2) !=0:
        value = current_slider_value  # 保持手动选择的范围
        return figure, max_minutes, marks, f"当前最大时间: {max_time.strftime('%H:%M')}", value, manual_clicks
    elif manual_clicks % 2 ==0:
        # 自动更新slider的值到最大值
        value = [slider_range[0], max_minutes]  # 自动显示最新的数据
        return figure, max_minutes, marks, f"当前最大时间: {max_time.strftime('%H:%M')}", value, manual_clicks

# 启动应用
if __name__ == '__main__':
    app.run_server(debug=True)
