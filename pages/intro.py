import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path = '/')
layout = html.Div(
        [
            dbc.Card(
                [
                    dbc.CardHeader(
                        html.H3("Welcome!")
                    ),
                    dbc.CardBody(
                        dcc.Markdown(
        """
            Welcome to this demographic data visualisation app!
        """
                        )
                    )
                ],
                className = 'mb-3'
            ),
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Getting started")),
                    dbc.CardBody(
                        dcc.Markdown(
        """
            Just click on either the 2D or 3D visualisation tabs to get started
        """
                        )
                    )
                ],
                className = "mb-3"
            )
        ],
        style = {
            "max-width" : "80%",
            "margin-left" : "5%"
        }
    )

