from dash import html, dcc, callback, Input, Output, State
import  dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

import json

from src.dynamic.canvas_2d_births import canvas2dBirths
from src.dynamic.canvas_2d_deaths import canvas2dDeaths
from src.dynamic.canvas_2d_exposures import canvas2dExposures
from src.dynamic.canvas_2d_population import canvas2dPopulation
from src.dynamic.canvas_2d_lifetables import canvas2dLifetables

with open('assets/lookups/types_of_data.json', 'r') as f:
    dataTypes = json.load(f)

with open('assets/lookups/places_by_type.json', 'r') as f:
    placesTypes = json.load(f)

def layout2dVisualisation():
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Dropdown(
                                options = dataTypes,
                                value = dataTypes[0]['value'],
                                id = "2d-type-selector"
                            ),
                            dbc.Tooltip("Select the type of demographic data to visualise",
                                        target = "2d-type-selector"
                            )
                        ],
                        width = 3
                    ),
                    dbc.Col(
                        [
                        dcc.Dropdown(
                            options = placesTypes[list(placesTypes.keys())[0]],
                            value =placesTypes[list(placesTypes.keys())[0]][0]['value'],
                            id = "2d-place-selector"
                        ),
                        dbc.Tooltip("Select which population to visualise",
                                    target = "2d-place-selector"
                        )
                        ],
                        width = 3
                    ),
                    dbc.Col(
                        [
                        dcc.RadioItems(
                            options = [
                                {"label" : "Males", "value" : "male"},
                                {"label" : "Females", "value" : "female"},
                                {"label" : "Total", "value" : "total"}
                            ],
                            value = "total",
                            inline = True,
                            id = "2d-sex-selector",
                            inputStyle = {
                                "margin" : "0.5rem",
                                "padding" : "0.5rem"
                                }
                        ),
                        dbc.Tooltip(
                            "Select which sex or sexes to visualise",
                            target = "2d-sex-selector"
                        )
                        ],
                        width = 3        
                    ),
                    dbc.Col(
                        [
                        dbc.Button("Go!", color = "success", className = "me1",
                            id = "2d-confirm-selection", n_clicks = 0
                        ),
                        dbc.Tooltip(
                            "After making selection, click to render visualisation",
                            target = "2d-confirm-selection"
                        )
                        ],
                        width = 2
                    ),
                    dbc.Col(
                        [
                            dbc.Button("More", color = "secondary", className = "me1",
                                       id = "2d-open-more", n_clicks = 0
                        ),
                        dbc.Tooltip(
                            "Click here to open additional options",
                            target = "2d-open-more-options"
                        ),
                        dbc.Offcanvas(
                            children = [
                                dbc.Placeholder(),
                                html.P("contents will go here ")
                            ],
                            title = "Further options",
                            id = "2d-more-options",
                            is_open=False,
                            placement = "end"
                        )
                        ]
                    )
                    
                ],
                className = "mb-2"
            ),
            dbc.Row(
                dbc.Col(
                    dcc.Graph(
                        id = "2d-vis-selection-output",
                        figure = {},
                        style={
                            'width': '100vh', 'height': '80vh'
                        }
                    ),
                    style = {
                        "flex-grow" : "1"
                    }
                ),
            )
        ],
        style = {
            "display": "flex",
            "flex-direction" : "column",
            "height" : "100%"
        }
    )

@callback(
    Output("2d-vis-selection-output", component_property="figure"),
    [Input("2d-confirm-selection", "n_clicks")],
    State("2d-type-selector", "value"),
    State("2d-place-selector", "value"),
    State("2d-sex-selector", "value")
)
def showSelection(n_clicks, type_value, place_value, sex_value):
    if (type_value == "births"):
        return canvas2dBirths(place_value, sex_value)

    elif (type_value == "deaths"):
        return canvas2dDeaths(place_value, sex_value)

    elif (type_value == 'exposures'):
        return canvas2dExposures(place_value, sex_value)

    elif (type_value == 'population'):
        return canvas2dPopulation(place_value, sex_value)
    elif (type_value == 'lifetables'):
        return canvas2dLifetables(place_value, sex_value)

    else: 
        return None
        

# Note this returns two outputs, first is options and second is values
@callback(
    Output('2d-place-selector', "options"),
    Output('2d-place-selector', 'value'),
    Input('2d-type-selector', "value")
)
def updatePlaceSelector(newPlace):
    return placesTypes[newPlace],placesTypes[newPlace][0]['value']

@callback(
    Output("2d-more-options", "is_open"),
    Input("2d-open-more", "n_clicks"),
    State("2d-more-options", "is_open")
)
def toggleMoreOptionsOffside(n1, is_open):
    if n1:
        return not is_open
    return is_open

