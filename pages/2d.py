
import dash
from dash import html, dcc, callback, Input, Output, State
import dash_bootstrap_components as dbc


import json

from utils.Make2dGraph import make2dGraph
from utils.Extract2dDataSeries import extract2dDataSeries



with open('assets/lookups/types_of_data.json', 'r') as f:
    dataTypes = json.load(f)

with open('assets/lookups/places_by_type.json', 'r') as f:
    placesTypes = json.load(f)

dash.register_page(__name__)

def viz2dMainOptions(dataTypes, placesTypes):
    return  dbc.Row(
                [
                    dbc.Col(
                        [
                            dcc.Dropdown(
                                options = dataTypes,
                                value = dataTypes[0]['value'],
                                id = "2d-type-selector",
                                multi=False
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
                            id = "2d-place-selector",
                            multi=True
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
                            "Select which sex to visualise",
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
            )

def viz2dDisplayMain():
    return  dbc.Row(
        children = [
            dbc.Col(
                children = [],
                id = '2d-viz-display-main',
                style={
                    'height': '75vh'
                },
                width = 8
            ),
            dbc.Col(
                html.Div(
                    children = [
                        dbc.Card(
                            body = True,
                            children = [
                                html.H4("Further options:", className = "card-title"),
                                dcc.Checklist(
                                    options = [
                                        {'label': ' Log y axis', 'value' : 'log-y'},
                                        {'label' : ' Show y from origin', 'value': "y-0"}
                                    ],
                                    value = [],
                                    id = 'fig-2d-y-options'
                                )                              
                                ],
                            style = {
                                "margin" : "1rem"
                            }
                        ),
                        dbc.Card(
                            body = True,
                            children = [
                                html.H4("More information:", className = 'card-title'),
                                html.P("Click on the graph to display more information here",
                                       id = 'fig-2d-clickonInfo')
                            ],
                            style = {
                                'margin' : '1rem'
                            }
                        )
                    ],
                    style = {
                        'height' : '75vh'
                    }
                ),
                width = 4
            )
        ],
        id = "2d-big-main"        
    )


layout = html.Div(
        [
            # This is a thin row with five columns:
                # dataType, placeTypes, sexes, Go, and More
            viz2dMainOptions(dataTypes, placesTypes),
            # This is a full height row containing two columns: 
            #    Viz2dDisplayMain and Viz2dDisplaySide
            viz2dDisplayMain()

        ],
        style = {
            "display": "flex",
            "flex-direction" : "column",
            "height" : "100%"
        }
    )



@callback(
    Output("2d-viz-display-main",  "children"),
    [Input("2d-confirm-selection", "n_clicks"),
    Input("fig-2d-y-options", "value")],
    State("2d-type-selector", "value"),
    State("2d-place-selector", "value"),
    State("2d-sex-selector", "value")
    
)
def showSelection(n_clicks, y_option_values, type_value, place_value, sex_value):
    # print("Show selection called")
    # print(f"type_value: {type_value}")
    # print(f"place_value: {place_value}")
    # print(f"sex_value: {sex_value}")
    # print(f"y_option_values : {y_option_values}")

    logY = "log-y" in y_option_values
    origY = "y-0" in y_option_values
    # If place_value is not a list, turn it into a list 
    if isinstance(place_value, str):
        place_value = [place_value]
    
    if type_value == "births":
        print(f"place: {place_value}, sex: {sex_value}")
        yearSeries, ySeriesDict = extract2dDataSeries(type_value, place_value, sex_value)
        fig = make2dGraph("Number of births over time", "year", "number of births", logY, origY, yearSeries, ySeriesDict)
        return dcc.Graph(
            figure = fig,
            id = 'clickable-2d-plot',
            style = {
                "width" : "100%",
                "height" : "100%"
            }
        )
    elif type_value == "deaths": 
        print("deaths type detected")
        yearSeries, ySeriesDict = extract2dDataSeries(type_value, place_value, sex_value)
        fig = make2dGraph("Number of deaths over time", "year", "number of deaths", logY, origY, yearSeries, ySeriesDict)
        return dcc.Graph(
            figure = fig,
            id = 'clickable-2d-plot',

            style = {
                "width" : "100%",
                "height" : "100%"
            }
        )
    elif type_value == 'exposures':
        print('exposures type detected')
        yearSeries, ySeriesDict = extract2dDataSeries(type_value, place_value, sex_value)
        fig = make2dGraph("Exposures over time", "year", "number of exposures", logY, origY, yearSeries, ySeriesDict)
        return dcc.Graph(
            figure = fig,
            id = 'clickable-2d-plot',
            style = {
                "width" : "100%",
                "height" : "100%"
            }
        )
    elif type_value == 'lifetables':
        print('exposures type detected')
        yearSeries, ySeriesDict = extract2dDataSeries(type_value, place_value, sex_value)
        fig = make2dGraph("Life expectancy at birth over time", "year", "life expectancy", logY, origY, yearSeries, ySeriesDict)
        return dcc.Graph(
            figure = fig,
            id = 'clickable-2d-plot',
            style = {
                "width" : "100%",
                "height" : "100%"
            }
        )
    elif type_value == 'population': 
        print("population type detected")
        yearSeries, ySeriesDict = extract2dDataSeries(type_value, place_value, sex_value)
        fig = make2dGraph("Total population over time", "year", "life expectancy", logY, origY, yearSeries, ySeriesDict)
        return dcc.Graph(
            figure = fig,
            id = 'clickable-2d-plot',
            style = {
                "width" : "100%",
                "height" : "100%"
            }
        )
    elif type_value == "Mx":
        print("Mx type detected")
        return html.P(
            "Mortality rates not implemented in 2d visualisation"
        )

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

@callback(
    Output('fig-2d-clickonInfo', 'children'),
    Input('clickable-2d-plot', 'clickData')
)
def showClickonInfo(clickData):
    print("triggered!")

    if clickData is not None:
        print(clickData)
        print(f"clickData has length {len(clickData['points'])}")
        print(clickData['points'][0]['x'])
        selectedYear = clickData['points'][0]['x']
        selectedValue = "{:.2f}".format(clickData['points'][0]['y'])
        return f"In {selectedYear} the value was {selectedValue}"
