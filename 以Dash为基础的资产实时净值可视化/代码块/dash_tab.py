

import dash_html_components as html
import dash_core_components as dcc


def get_tab(data_dict):

    id_name1 = 'historical_dynamic'
    id_name2 = 'historical_revenue'


    historical_dynamic = data_dict[id_name1]
    length_slider = len(historical_dynamic.index)

    historical_revenue = data_dict[id_name2]
    length_slider2 = len(historical_revenue)

    tab = html.Div([
        # graph 1
        html.Div([
            html.Div('产品历史资产净值', className="title2",style={"font-size": "40px", "font-weight": "bold"}),
            html.Hr(),
            dcc.Graph(id='historical_dynamic', className="graph-m"),
            dcc.RangeSlider(
                id='slider-dynamic-info',
                marks={i: f"{historical_dynamic.index[i]}" for i in range(0,length_slider,5)},
                min=0,
                max=length_slider,
                value=[0,length_slider]),
            ], className='div-graph-unit'),
        html.Br(),
        # graph 2
        html.Div([
            html.Div('产品历史资产涨跌幅', className="title2",style={"font-size": "40px", "font-weight": "bold"}),
            html.Hr(),
            dcc.Graph(id='historical_revenue', className="graph-m"),
            dcc.RangeSlider(
                id='slider-revenue-info',
                marks={i: f"{historical_revenue.index[i]}" for i in range(0,length_slider2,5)},
                min=0,
                max=length_slider,
                value=[0,length_slider2]),
            ], className='div-graph-unit'),
        html.Br(),
        # graph3
        html.Div([
            html.Div('产品实时资产涨跌幅', className="title2",style={"font-size": "40px", "font-weight": "bold"}),
            html.Hr(),
            dcc.Graph(id='daily_revenue', className="graph-m"),
            dcc.Interval(id='interval',interval=60000,n_intervals=0)])

        ])
    return tab

