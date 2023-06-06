import pandas as pd

from dash import html, Dash, dcc, Input, Output, State, callback


dta_mx = pd.read_csv('assets/data/Mx.csv')
countries_kv = dta_mx[
        ["country", "cntry"]
    ].drop_duplicates(
    ).set_index(
        'country'
    ).to_dict(
    )['cntry']

lookupsCountries = [{'label': key, 'value': value} for key, value in countries_kv.items()]    
lookupsCountries


def showLabelledcountriesGeneratedFromData():
    return html.Div([
        html.H4("Country selected based on data"),
        html.P("""
        The aim of this feature test is to confirm that I can generate a labelled dropdown 
        selection of countries and show that the value (not the labelled) is being returned
        """),
        dcc.Dropdown(
            options = lookupsCountries,
            value = lookupsCountries[0].get('value'),
            id = 'countries-labelled-dropdown'
        ),
        html.Div(
            id = 'countries-option-output-container'
        )
    ])

@callback(
    Output('countries-option-output-container', 'children'),
    Input('countries-labelled-dropdown', 'value')
)
def update_output(value):
    return f'you have selected {value}'