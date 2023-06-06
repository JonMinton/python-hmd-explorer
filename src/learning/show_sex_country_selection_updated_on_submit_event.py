import pandas as pd

from dash import html, Dash, dcc, Input, Output, State, callback

dta_mx = pd.read_csv('assets/data/Mx.csv')

countries_kv = dta_mx[
        ["country", 'cntry']
    ].drop_duplicates(
    ).set_index(
        'country'
    ).to_dict(
    )['cntry']

lookupsCountries = [{'label':key, 'value':value} for key, value in countries_kv.items()]

lookupsSexes = [
    {'label': 'Male', 'value':'male'},
    {'label': 'Female', 'value':'female'},
    {'label': 'Total', 'value':'total'}
]

def showSexCountrySelectionUpdatedOnSubmitEvent():
    return html.Div([
        html.H4("Country and sex selection updated on submit event"),
        html.P("""
            The aim of this feature test is to show that both sex and country options can 
            be generated from the available data, and only sent on the clicking of a submit button rather
            than on change to either selection
        """),
        dcc.Dropdown(
            options = lookupsCountries,
            value = lookupsCountries[0].get('value'),
            id = 'countries-labelled-dropdown-as-state'
        ),
        dcc.Dropdown(
            options = lookupsSexes,
            value = lookupsSexes[2].get('value'),
            id = 'sexes-labelled-dropdown-as-state'
        ),

        html.Button(
            'Confirm selection', 
            id = "selection-submit-button"
        ),
        html.Div(
            id = 'countries-sexes-option-output-container'
        )
    ])

@callback(
    Output('countries-sexes-option-output-container', 'children'),
    [Input('selection-submit-button', 'n_clicks')],
    [
        State('countries-labelled-dropdown-as-state', 'value'),
        State('sexes-labelled-dropdown-as-state', 'value')    
    ]
)
def update_output(n_clicks, value_country, value_sex):
    return f'you have selected country {value_country} and sex {value_sex}'