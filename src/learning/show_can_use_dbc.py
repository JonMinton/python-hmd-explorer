import dash_bootstrap_components as dbc
from dash import html


def showCanUseDbc():
    return html.Div(
    [
        dbc.Row(
            dbc.Col(html.Div("A single column")),
        ),
        dbc.Row(
            [
                dbc.Col(html.Div("One of three columns")),
                dbc.Col(html.Div("One of three columns", style = {"background-color": 'rgba(0, 255, 0, 0.5)'})),
                dbc.Col(html.Div("One of three columns"))
            ]
        )
    ],
    style = {"background-color": 'rgba(255, 0, 0, 0.5)'}
    )