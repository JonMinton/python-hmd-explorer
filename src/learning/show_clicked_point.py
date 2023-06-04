import json
from dash import Dash, html, dcc, callback
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd

df = px.data.iris()

fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
fig.update_layout(clickmode='event+select')

def showClickedPoint():
    return html.Div([
        html.H4('Show simple 3d plot'),
        html.P("The aim of this feature test is to show a simple 3d plotly plot"),
        dcc.Graph(id = 'clickable-3d-plot', figure = fig),
            html.Div(className='row', children=[
        html.Div([
            dcc.Markdown("""
                **Hover Data**
            """),
            html.Div(id='hover-data')
        ], className='three columns'
        ),

        html.Div(
        [
            dcc.Markdown("""
            **Click Data**
            """),
            html.Div(id='click-data')            
        ],
        className='three columns'
        )
    ])

    ])


styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}




@callback(
    Output('hover-data', 'children'),
    Input('clickable-3d-plot', 'hoverData'))
def display_hover_data(hoverData):
    if hoverData is not None:
        return 'Hovered: x={}, y={}, z={}'.format(
            hoverData['points'][0]['x'],
            hoverData['points'][0]['y'],
            hoverData['points'][0]['z']
        )


@callback(
    Output('click-data', 'children'),
    Input('clickable-3d-plot', 'clickData'))
def display_click_data(clickData):
    if clickData is not None:
        return 'Clicked: x={}, y={}, z={}'.format(
            clickData['points'][0]['x'],
            clickData['points'][0]['y'],
            clickData['points'][0]['z']
        )


