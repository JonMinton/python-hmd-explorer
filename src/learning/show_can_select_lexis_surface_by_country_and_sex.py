import pandas as pd
import numpy as np

from dash import html, Dash, dcc, Input, Output, State, callback

import plotly.graph_objects as go

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

def showLexisSurfaceBasedOnUserCountryAndSexSelection():
    return html.Div([
        html.H4("Lexis surface based on user country and sex selection"),
        html.P("""
            The aim of this feature test is to show a Lexis surface being generated
            based on a user selection of country and sex which is only 
            confirmed when a button is pressed.
        """),
        dcc.Dropdown(
            options = lookupsCountries,
            value = lookupsCountries[0].get('value'),
            id = 'lexis-countries-labelled-dropdown-as-state'
        ),
        dcc.Dropdown(
            options = lookupsSexes,
            value = lookupsSexes[2].get('value'),
            id = 'lexis-sexes-labelled-dropdown-as-state'
        ),

        html.Button(
            'Confirm selection', 
            id = "lexis-selection-submit-button"
        ),
        dcc.Graph(
            figure = {}, 
            id = 'countries-sexes-option-lexis-container'
        )
    ])


@callback(
    Output('countries-sexes-option-lexis-container', 'figure'),
    [Input('lexis-selection-submit-button', 'n_clicks')],
    [
        State('lexis-countries-labelled-dropdown-as-state', 'value'),
        State('lexis-sexes-labelled-dropdown-as-state', 'value')    
    ]
)
def update_output(n_clicks, value_country, value_sex):
    df_ss = dta_mx[
        (dta_mx['cntry'] == value_country) & 
        (dta_mx['sex'] == value_sex) & 
        (dta_mx['age'] <= 90)
    ]
    df_ss.reset_index(drop = True)
    # print(df_ss.head())
    # This is the smallest observed mx
    min_mx = df_ss['mx'][df_ss["mx"] > 0].min()
    # print("min_mx is " + "{:.5f}".format(min_mx))

    mx_array = df_ss[
        ['age', 'year', 'mx']
    ].pivot(
        index = 'year', columns = 'age', values = 'mx'
    )
    mx_array = np.array(mx_array)
    # For values 
    mx_array = np.where(mx_array == 0, min_mx, mx_array)
    # mx_array = np.where(np.isnan(mx_array), min_mx, mx_array)


    fig = go.Figure(data = [
        go.Surface(
            z = mx_array,
            surfacecolor = np.log(mx_array)
        )
    ])

    fig.update_layout(
        scene = dict(
            zaxis = dict(title = "Logged mortality", type="log"),
            xaxis = dict(title = "Age in years"),
            yaxis = dict(title = "Year")

        )
    )
    return fig