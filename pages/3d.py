import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import json

import plotly.graph_objects as go

from utils.Extract3dDataArrays import extract3dDataArrays
from utils.Make3dLexisSurface import make3dLexisSurface

with open('assets/lookups/types_of_data.json', 'r') as f:
    dataTypes = json.load(f)

with open('assets/lookups/places_by_type.json', 'r') as f:
    placesTypes = json.load(f)

dash.register_page(__name__)

def viz3dMainOptions(dataTypes, placesTypes):
    return  dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Dropdown(
                                options = dataTypes,
                                value = dataTypes[0]['value'],
                                id = "3d-type-selector",
                                multi=False
                            ),
                            dbc.Tooltip("Select the type of demographic data to visualise",
                                        target = "3d-type-selector"
                            )
                        ],
                        width = 2
                    ),
                    dbc.Col(
                        [
                        dcc.Dropdown(
                            options = placesTypes[list(placesTypes.keys())[0]],
                            value =placesTypes[list(placesTypes.keys())[0]][0]['value'],
                            id = "3d-place-selector",
                            multi=False
                        ),
                        dbc.Tooltip("Select which population to visualise",
                                    target = "3d-place-selector"
                        )
                        ],
                        width = 2
                    ),
                    dbc.Col(
                        [
                        dcc.RadioItems(
                            options = [
                                {"label" : "M", "value" : "male"},
                                {"label" : "F", "value" : "female"},
                                {"label" : "Total", "value" : "total"}
                            ],
                            value = "total",
                            inline = True,
                            id = "3d-sex-selector",
                            inputStyle = {
                                "margin" : "0.5rem",
                                "padding" : "0.5rem"
                                }
                        ),
                        dbc.Tooltip(
                            "Select which sex to visualise",
                            target = "3d-sex-selector"
                        )
                        ],
                        width = 2        
                    ),
                    dbc.Col(
                        children = [
                            dcc.RadioItems(
                                [
                                    {
                                        "label" : 
                                            html.Img(src = "assets/images/main-only.svg", height = 20),
                                        "value" : "main-only"
                                    },
                                    {
                                        "label" : html.Img(src = "assets/images/main-3colRight.svg", height = 20),
                                        "value" : "main-3col"
                                    },
                                    {
                                        "label" : html.Img(src = "assets/images/main-3rowBottom.svg", height = 20),
                                        "value" : "main-3row"
                                    }
                                ],
                            value = 'main-only',
                            inline = True,
                            id = "3d-canvas-setup",
                            inputStyle = {
                                "margin" : "0.5rem",
                                "padding" : "0.5rem"
                                }                                
                            ),
                        dbc.Tooltip(
                            "Select how display should be organised",
                            target = "3d-canvas-setup"
                        )
                        ],
                        width = 2
                    ),
                    dbc.Col(
                        children = [
                            dcc.RadioItems(
                                [

                                    {
                                        "label" : "H",
                                        "value" : "heatmap-only"
                                    },
                                    {
                                        "label" : "H+C",
                                        "value" : "contour-heatmap"
                                    },
                                    {
                                        "label" : "3D",
                                        "value" : "3d"
                                    }
                                ],
                                value = '3d',
                                inline = True,
                                id = "lexis-surface-style",
                                inputStyle = {
                                    "margin" : "0.5rem",
                                    "padding" : "0.5rem"
                                }                                
                            ),
                            dbc.Tooltip(
                                "Select how Lexis surface should be displayed",
                                target = "lexis-surface-style"
                            )
                        ],
                        width = 2
                    ),
                    dbc.Col(
                        [
                        dbc.Button("Go!", color = "success", className = "me1",
                            id = "3d-confirm-selection", n_clicks = 0
                        ),
                        dbc.Tooltip(
                            "After making selection, click to render visualisation",
                            target = "3d-confirm-selection"
                        )
                        ],
                        width = 1
                    ),
                    dbc.Col(
                        [
                            dbc.Button("More", color = "secondary", className = "me1",
                                       id = "3d-open-more", n_clicks = 0
                            ),
                            dbc.Tooltip(
                                "Click here to open additional options",
                                target = "3d-open-more-options"
                            ),
                            dbc.Offcanvas(
                                children = [
                                    dbc.Placeholder(),
                                    html.P("contents will go here ")
                                ],
                                title = "Further options",
                                id = "3d-more-options",
                                is_open=False,
                                placement = "end"
                            )
                        ],
                        width = 1
                    )
                    
                ],
                className = "mb-2"
            )


def viz3dDisplayMain():
    return  dbc.Row(
        children = [
            dbc.Col(
                children = [],
                id = '3d-viz-display-main',
                style={
                    'height': '75vh'
                },
                width = 8
            ),
            dbc.Col(
                html.Div(
                    children = [
                    ],
                    style = {
                        'height' : '75vh'
                    }
                ),
                width = 4
            )
        ],
        id = "3d-big-main"        
    )

layout = html.Div(
        [
            # This is a thin row with five columns:
                # dataType, placeTypes, sexes, Go, and More
            viz3dMainOptions(dataTypes, placesTypes),
            # This is a full height row containing two columns: 
            #    Viz2dDisplayMain and Viz2dDisplaySide
            viz3dDisplayMain()

        ],
        style = {
            "display": "flex",
            "flex-direction" : "column",
            "height" : "100%"
        }
    )

@callback(
    Output("3d-big-main", "children"),
    Input("3d-canvas-setup", "value"),
    Input("lexis-surface-style", "value")
)
def select3dCanvas(canvas_value, lexisStyle_value):
    print(f"canvas: {canvas_value}; LS: {lexisStyle_value}")
    if canvas_value == 'main-only':
        return dbc.Row(
            children = [
                dbc.Col(
                    id = 'lexis-surface-container',
                    style = {
                        "height" : "75vh",
                        "margin" : "0",
                        "padding" : "0"
                    },
                    width = 12
                )
            ]
        )
    elif canvas_value == "main-3col":
        return dbc.Row(
            children = [
                dbc.Col(
                    id = 'lexis-surface-container',
                    width = 8,
                    style = {
                        "height" : "75vh"
                    }
                ),
                dbc.Col(
                    children = [
                        dcc.Graph(
                            figure = {},
                            id = "subplot-age",
                            style = {
                                "height" : "100%",
                                "width" : "100%"
                            }
                        ),
                        dcc.Graph(
                            figure = {},
                            id = "subplot-period",
                            style = {
                                "height" : "100%",
                                "width" : "100%"
                            }
                        ),
                        dcc.Graph(
                            figure = {},
                            id = "subplot-cohort",
                            style = {
                                "height" : "100%",
                                "width" : "100%"
                            }
                        )

                    ],
                    width = 4,
                    style = {
                        "display" : "flex",
                        "flex-direction" : "column"
                    }
                )
            ]
        )
    elif canvas_value == "main-3row":
        return html.Div(
            children = [
                        dbc.Row(
                            children = [
                                dbc.Col(
                                    id = 'lexis-surface-container'
                                )
                            ],
                            style = {
                                "height" : "40vh"
                            }
                        ),
                        dbc.Row(
                            children = [
                                dbc.Col(
                                    children = [
                                        dcc.Graph(
                                            figure = {},
                                            id = "subplot-age",
                                            style = {
                                                "height" : "100%",
                                                "width" : "100%"
                                            }
                                        )
                                    ],
                                    width = 4
                                ),
                                dbc.Col(
                                    children = [
                                        dcc.Graph(
                                            figure = {},
                                            id = "subplot-period",
                                            style = {
                                                "height" : "100%",
                                                "width" : "100%"
                                            }
                                        )
                                    ],
                                    width = 4
                                ),
                                dbc.Col(
                                    children = [
                                        dcc.Graph(
                                            figure = {},
                                            id = "subplot-cohort",
                                            style = {
                                                "height" : "100%",
                                                "width" : "100%"
                                            }
                                        )
                                    ],
                                    width = 4
                                ),

                            ],
                            style = {
                                "margin": "0",
                                "padding" : "0"
                            }
                        )                
            ]
             
        )


@callback(
    Output('lexis-surface-container', 'children'),
    Input('3d-confirm-selection', 'n_clicks'),
    State('3d-type-selector', 'value'),
    State('3d-place-selector', 'value'),
    State('3d-sex-selector', 'value'),
    State('lexis-surface-style', 'value')
)
def generateAppropriateLexisSurface(n_clicks, typeValue, placeValue, sexValue, styleValue):
    print(f"generating Lexis surface for {typeValue}")
    print(f"placeValue: {placeValue}")
    print(f"sexValue: {sexValue}")

    if typeValue == 'births':
        return html.P(
            "Lexis surfaces not implemented for births"
        )
    elif typeValue == 'deaths':
        xRange, yRange, zArray = extract3dDataArrays(typeValue, sexValue, placeValue)
        fig = make3dLexisSurface(styleValue, 'Age in years', 'Year', 'Number of deaths', "Lexis surface of number of deaths", xRange, yRange, zArray, True)
        return dcc.Graph(
             figure = fig,
             id = 'lexis-surface',
             style = {
                  'height' : '100%',
                  'width' : '100%'
             }
        )
    elif typeValue == 'exposures':
        xRange, yRange, zArray = extract3dDataArrays(typeValue, sexValue, placeValue)
        fig = make3dLexisSurface(styleValue, 'Age in years', 'Year', 'Number of exposures', "Lexis surface of number of exposures", xRange, yRange, zArray, False)
        return dcc.Graph(
             figure = fig,
             id = 'lexis-surface',
             style = {
                  'height' : '100%',
                  'width' : '100%'
             }
        )
    elif typeValue == 'Mx':
        print("I'm in Mx main")
        xRange, yRange, zArray = extract3dDataArrays(typeValue, sexValue, placeValue)
        fig = make3dLexisSurface(styleValue, 'Age in years', 'Year', 'Mortality Rate', "Mortality Rate Lexis surface", xRange, yRange, zArray, True)
        return dcc.Graph(
             figure = fig,
             id = 'lexis-surface',
             style = {
                  'height' : '100%',
                  'width' : '100%'
             }
        )
    elif typeValue == 'population':
        xRange, yRange, zArray = extract3dDataArrays(typeValue, sexValue, placeValue)
        fig = make3dLexisSurface(styleValue, 'Age in years', 'Year', 'Population Size', "Population Size Lexis surface", xRange, yRange, zArray, False)
        return dcc.Graph(
             figure = fig,
             id = 'lexis-surface',
             style = {
                  'height' : '100%',
                  'width' : '100%'
             }
        )
    elif typeValue == 'lifetables':
        xRange, yRange, zArray = extract3dDataArrays(typeValue, sexValue, placeValue)
        fig = make3dLexisSurface(styleValue, 'Age in years', 'Year', 'Life Expectancy', "Age conditional Life expectancy Lexis Surface", xRange, yRange, zArray, False)
        return dcc.Graph(
             figure = fig,
             id = 'lexis-surface',
             style = {
                  'height' : '100%',
                  'width' : '100%'
             }
        )
    



