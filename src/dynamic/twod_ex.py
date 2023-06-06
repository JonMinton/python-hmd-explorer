import pickle
import plotly.express as px
import pandas as pd

from dash import html, dcc, Dash, dash_table, Input, Output, callback


with open('assets/lookups/sexes.pkl', 'rb') as f:
    lookupsSex = pickle.load(f)

with open('assets/lookups/countries.pkl', 'rb') as f:
    lookupsCountries = pickle.load(f)

# This is the format expected to be able to display a label but return the value
lookupsCountriesLv = [{'label': key, 'value': value} for key, value in lookupsCountries.items()]    

# print(lookupsCountriesLv)
# print(lookupsCountriesLv[1]['value'])

df = pd.read_csv('assets/data/lifetables.csv')
   
def section2dEx():
    return html.Div([
        html.H4('tab-inner-2d-ex IN MODULE'),
        dcc.Dropdown(
            options = lookupsSex, 
            value = lookupsSex[1], 
            id='sexSelectInput'
        ),
        dcc.Dropdown(
            options=lookupsCountriesLv, 
            value = lookupsCountriesLv[1], 
            id='countriesSelectInput'
        ),
        html.Div(id='bothSelectOutput'),
        html.Div(f'The df has {df.shape[0]} rows and {df.shape[1]} columns'),
        html.Div(id='bothSelectFilteredDf')
    ])





@callback(
    Output('bothSelectOutput', 'children'),
    [
        Input('sexSelectInput', 'value'),
        Input('countriesSelectInput', 'value')
    ]
)
def update_output(sexSelectInput_value, countriesSelectInput_value):
    return f'You have selected sex {sexSelectInput_value} and country {countriesSelectInput_value}'

@callback(
    Output('bothSelectFilteredDf', 'children'),
    [
        Input('sexSelectInput', 'value'),
        Input('countriesSelectInput', 'value')
    ]
)
def filter_df(sexSelectInput_value, countriesSelectInput_value):
    df_filtered = df[
        (df['sex'] == sexSelectInput_value) &
        (df['country'] == countriesSelectInput_value)
    ]
    return f'The filtered df has {df_filtered.shape[0]} rows and {df_filtered.shape[1]} columns'
