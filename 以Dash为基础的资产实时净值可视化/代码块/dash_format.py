import plotly.graph_objs as go
from dash2.const_gui import *
def format_figure(fig, y=False, title=None, dtick=None, line_width=pic_line_w, mode=None,
                  legend_x=pic_le_x, legend_y=pic_le_y, xaxes_title=None, yaxes_title=None,
                  xaxes_visible=True, yaxes_visble=True, zeroline=False,
                  m_t=pic_m_t, m_b=pic_m_b, m_l=pic_m_l, m_r=pic_m_r):
    fig.update_layout(
        margin={"t": m_t + 20 if title else m_t, 'b': m_b, 'l': m_l, 'r': m_r},
        showlegend=True,
        legend=go.layout.Legend(x=legend_x, y=legend_y, tracegroupgap=2),
        hovermode=pic_hover_mode
    )
    if title:
        fig.update_layout(
            title=dict(text=title, x=0.5, font=dict(size=12))
        )

    if y:
        fig.update_layout(
            yaxis2=dict(anchor='x', overlaying='y', side='right'),
        )

    fig.update_traces(hovertemplate='%{y}')

    if mode:
        fig.update_traces(mode=mode)

    fig.update_xaxes(
        title=xaxes_title,
        dtick=dtick,
        tickformat=pic_date_format,
        visible=xaxes_visible,
    )

    if zeroline:
        fig.update_xaxes(
            zeroline=True,
            zerolinecolor="black",
            zerolinewidth=2
        )

    fig.update_yaxes(
        title=yaxes_title,
        visible=yaxes_visble,
    )

    if line_width:
        for d in fig.data:
            if isinstance(d, go.Scatter):
                d.line = dict(width=line_width)
    return fig
