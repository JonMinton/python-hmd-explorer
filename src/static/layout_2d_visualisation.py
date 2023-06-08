from dash import html, dcc, callback, Input, Output, State
import  dash_bootstrap_components as dbc

import json

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
                        width = 3
                    )
                    
                ],
                className = "mb-2"
            ),
            dbc.Row(
                dbc.Col(
                    html.P("", 
                        id = "2d-vis-selection-output",
                        style = {
                            "background-color" : "cyan",
                            "height" : "100%"
                            }               
                        )
                ),
                style = {
                    "flex-grow" : "1"
                }
            ),
        ],
        style = {
            "display": "flex",
            "flex-direction" : "column",
            "height" : "100%"
        }
    )

@callback(
    Output("2d-vis-selection-output", component_property="children"),
    [Input("2d-confirm-selection", "n_clicks")],
    State("2d-type-selector", "value"),
    State("2d-place-selector", "value"),
    State("2d-sex-selector", "value")
)
def showSelection(n_clicks, type_value, place_value, sex_value):
    return f"Clicked {n_clicks} times and selected type {type_value}, place {place_value}, and sex {sex_value}"

# Note this returns two outputs, first is options and second is values
@callback(
    Output('2d-place-selector', "options"),
    Output('2d-place-selector', 'value'),
    Input('2d-type-selector', "value")
)
def updatePlaceSelector(newPlace):
    return placesTypes[newPlace],placesTypes[newPlace][0]['value']
    
