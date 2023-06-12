from dash import dcc, html
import dash_bootstrap_components as dbc

def viz2dDisplayMain():
    return  dbc.Row(
        children = [
            dbc.Col(
                children = [],
                id = '2d-viz-display-main',
                style={
                    'height': '75vh',
                    'border-width' : '1px',
                    'border-style' : 'solid',
                    'border-color': 'red'
                },
                width = 8
            ),
            dbc.Col(
                html.Div(
                    children = [
                        html.P("text for sidebar")
                    ],
                    style = {
                        'border-width': '1px',
                        'border-style' : 'solid',
                        'border-color' : 'black',
                        'height' : '75vh'
                    }
                ),
                width = 4
            )
        ]        
    )
        



