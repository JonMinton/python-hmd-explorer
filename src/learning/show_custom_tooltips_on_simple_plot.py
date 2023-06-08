import pandas as pd

from dash import html, dcc, callback
import plotly.graph_objects as go

d = pd.read_csv("assets/data/Mx.csv")
d2 = d[
    (d['sex'] == 'female') &
    (d['cntry'] == 'USA') & 
    (d['age'] == 0)
    ]
#

d2['text'] = d2.apply(
    lambda x: "In %s at age %s the %s mortality rate was %1.4f" % (
        x['year'], x['age'], x['sex'], x['mx']
    ), axis = 1
)

figo = go.Figure()

figo.add_trace(
    go.Scatter(
        x = d2['year'],
        y = d2['mx'],
        text = d2['text'],
        fill = 'tozeroy',
        hovertemplate = '%{text}'
    )
)
figo.update_layout(
    xaxis_title = 'Year',
    yaxis_title = "Mx",
    yaxis_type = 'log'
)


def showCustomTooltipsOnSimplePlot():
    return html.Div([
        html.H4("Show custom hovertext on simple plot"),
        html.P("The aim of this feature test is to show custom text on a simple graph"),
        dcc.Graph(figure = figo)
    ])