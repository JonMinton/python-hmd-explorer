from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

with open('assets/lookups/types_of_data.json', 'r') as f:
    dataTypes = json.load(f)

with open('assets/lookups/places_by_type.json', 'r') as f:
    placesTypes = json.load(f)

def layout3dVisualisation():
    return html.Div(
        dbc.Row(
            [
                dbc.Col(
                [
                    dcc.Dropdown(
                        options = dataTypes,
                        value = dataTypes[0]['value'],
                        id = "3d-type-selector"
                    ),
                    dbc.Tooltip("Select the type of demographic data to visualise",
                        target = "3d-type-selector"
                    )
                ], 
                width = 3        
                ),
                dbc.Col([
                    dcc.Dropdown(
                        options = placesTypes[list(placesTypes.keys())[0]],
                        value =placesTypes[list(placesTypes.keys())[0]][0]['value'],
                        id = "3d-place-selector"
                    ),
                    dbc.Tooltip("Select which population to visualise",
                                target = "3d-place-selector"
                    )
                ], width = 3),
                dbc.Col([
                    dcc.RadioItems(
                        options = [
                            {"label" : "Males", "value" : "male"},
                            {"label" : "Females", "value" : "female"},
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
                        "Select which sex or sexes to visualise",
                        target = "3d-sex-selector"
                    )


                ], width = 3),
                dbc.Col([
                    dbc.Button("Go!", color = "success", className = "me1",
                        id = "2d-confirm-selection", n_clicks = 0
                    ),
                    dbc.Tooltip(
                        "After making selection, click to render visualisation",
                        target = "2d-confirm-selection"
                    )
                ], width = 3)                
            ]


        )
    )