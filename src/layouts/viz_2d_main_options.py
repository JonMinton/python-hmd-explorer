from dash import dcc, html
import dash_bootstrap_components as dbc

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
                        dcc.Checklist(
                            options = [
                                {"label" : "Males", "value" : "male"},
                                {"label" : "Females", "value" : "female"},
                                {"label" : "Total", "value" : "total"}
                            ],
                            value = ["total"],
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
            )
