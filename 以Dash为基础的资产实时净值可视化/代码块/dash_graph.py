import datetime
import plotly.graph_objects as go

from dash_format import format_figure

def amends_data():
    pass


def scatter_graph(df,value:str,*args):
    traces = []
    traces2 = []
    colors = ['blue', 'red', 'green', 'orange', 'purple']
    if not args:
        for product_name,data in df.iteritems():
            trace = go.Scatter(
            x = data.index,
            y = data,
                mode='lines+markers',
                name=f'{product_name}{value}曲线',
                line=dict(color=colors[df.columns.get_loc(product_name) % len(colors)], width=2, shape='spline'),
            )
            traces.append(trace)
    else:
        start = int(args[0])
        end = int(args[1])

        for product_name,data in df.iteritems():

            trace = go.Scatter(
            x = data.index[start:end],
            y = data[start:end],
                mode='lines+markers',
                name=f'{product_name}{value}曲线',
                line=dict(color=colors[df.columns.get_loc(product_name) % len(colors)], width=2, shape='spline'),
            )
            traces.append(trace)

            data = data.astype(float)
            df_y = (data+1/(float(data.iloc[int(start)])+1))-1

            trace2 = go.Scatter(
                x=data.index[start:end],
                y=df_y.iloc[start:end],
                mode='lines+markers',
                name=f'{product_name}{value}曲线',
                line=dict(color=colors[df.columns.get_loc(product_name) % len(colors)], width=2, shape='spline'),
            )
            traces2.append(trace2)
    return [traces,traces2]

# 三幅图，三个要求
def dash_slider_1(data_dict, va):

    yr_start = va[0]
    yr_end = va[1]
    id_name1 = 'historical_dynamic'

    df = data_dict[id_name1]
    traces = scatter_graph(df,'历史净值',yr_start,yr_end)[0]

    fig = go.Figure(data=traces)
    fig = format_figure(fig, y=False)
    return fig


def dash_slider_2(data_dict,va):
    yr_start = va[0]
    yr_end = va[1]
    id_name1 = 'historical_revenue'

    df = data_dict[id_name1]
    traces = scatter_graph(df,'历史涨跌幅',yr_start,yr_end)[1]

    fig = go.Figure(data=traces)
    fig = format_figure(fig, y=False)
    return fig

def dash_graph_3(data_dict):
    id_name3 = 'daily_revenue'
    daily_revenue = data_dict[id_name3]
    traces = scatter_graph(daily_revenue,'当日涨跌幅')[0]
    fig = go.Figure(data=traces)
    fig = format_figure(fig, y=False)
    print('数据实时更新完毕')
    return fig
