from dash import html, dcc, Output, Input, callback
import plotly.graph_objects as go
import pandas as pd
import numpy as np

df = pd.read_csv("assets/data/mx.csv")
df_ss = df[
    (df['cntry'] == 'USA') & 
    (df['sex'] == 'female')
]
df_ss.reset_index(drop = True)

mx_array = df_ss[
    ['age', 'year', 'mx']
].pivot(
    index = 'year', columns = 'age', values = 'mx'
)
mx_array = np.array(mx_array)

fig = go.Figure(data = [
    go.Surface(
        z = mx_array,
        surfacecolor = np.log(mx_array)
    )
])

fig.update_layout(
    scene = dict(
        zaxis = dict(title = "Logged mortality", type="log"),
        xaxis = dict(title = "Age in years"),
        yaxis = dict(title = "Year")

    )
)

def showHoverClickOnLexisSurfacePlot():
    return html.Div([
        html.H4('Show Lexis Surface Plot'),
        html.P("The aim of this feature test is to confirm I can create a 3d surface plot of a downloaded population"),
        dcc.Graph(id = "clickable-lexis-surface", figure = fig),
        html.Div(id = 'hover-data-lexis'),
        html.Div(id = 'click-data-lexis')
    ])

@callback(
    Output('hover-data-lexis', 'children'),
    Input('clickable-lexis-surface', 'hoverData'))
def display_hover_data(hoverData):
    if hoverData is not None:
        return 'Hovered: x={}, y={}, z={}'.format(
            hoverData['points'][0]['x'],
            hoverData['points'][0]['y'],
            hoverData['points'][0]['z']
        )


@callback(
    Output('click-data-lexis', 'children'),
    Input('clickable-lexis-surface', 'clickData'))
def display_click_data(clickData):
    if clickData is not None:
        return 'Clicked: x={}, y={}, z={}'.format(
            clickData['points'][0]['x'],
            clickData['points'][0]['y'],
            clickData['points'][0]['z']
        )