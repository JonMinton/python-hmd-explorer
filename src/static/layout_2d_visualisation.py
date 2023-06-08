from dash import html, dcc, callback, Input, Output, State
import  dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

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
                    dcc.Graph(
                        id = "2d-vis-selection-output",
                        figure = {},
                        style={
                            'width': '100vh', 'height': '80vh'
                        }
                    ),
                #     html.P("", 
                #         id = "2d-vis-selection-output",
                #         style = {
                #             "background-color" : "cyan",
                #             "height" : "100%"
                #             }               
                #         )
                # ),
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
        dta = pd.read_csv("assets/data/births.csv")
        d2 = dta.loc[
            (dta['cntry'] == place_value) & 
            (dta['sex'] == sex_value), :
        ]
        fig = px.line(d2, x="year", y="number_of_births")
        return fig
    elif (type_value == "deaths"):
        dta = pd.read_csv("assets/data/deaths.csv")
        d2 = dta.loc[
            (dta['cntry'] == place_value) & 
            (dta['sex'] == sex_value)
        ]
        # The code below returns the total number of deaths by year
        d3 = d2.groupby(['year']).agg({"number_of_deaths" : "sum"}).reset_index()
        
        fig = px.line(d3, x = "year", y = "number_of_deaths")
        return fig
    elif (type_value == 'exposures'):
        dta = pd.read_csv("assets/data/exposures.csv")
        d2  = dta.loc[
            (dta['cntry'] == place_value) & 
            (dta['sex'] == sex_value), :
        ]
        d3 = d2.groupby(['year']).agg({"exposures_count" : "sum"}).reset_index()

        fig = px.line(d3, x = "year", y = "exposures_count")
        return fig
    elif (type_value == 'population'):
        dta = pd.read_csv("assets/data/population.csv")
        d2 = dta.loc[
            (dta['cntry'] == place_value) & 
            (dta['sex'] == sex_value), :
        ]
        d3 = d2.groupby(['year']).agg({"population_count" : "sum"}).reset_index()

        fig = px.line(d3, x = 'year', y = 'population_count')
        return fig
    elif (type_value == 'lifetables'):
        dta = pd.read_csv("assets/data/lifetables.csv")
        adj_sex_value = "both" if sex_value == "total" else sex_value
        d2 = dta.loc[
            (dta['cntry'] == place_value) & 
            (dta['sex'] == adj_sex_value) & 
            (dta['age'] == 0), :
        ]

        fig = px.line(d2, x= 'year', y = 'ex')
        return fig
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



