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

print(lookupsCountriesLv)
print(lookupsCountriesLv[1]['value'])

df = pd.read_csv('assets/data/lifetables.csv')
   
def section2dEx():
    return html.Div([
        html.H4('tab-inner-2d-ex IN MODULE'),
        dcc.Dropdown(
            lookupsSex, 
            lookupsSex[[1]], 
            id='sexSelectInput'
        ),
        dcc.Dropdown(
            lookupsCountriesLv, 
            lookupsCountriesLv[1]['label'], 
            id='countriesSelectInput'
        ),
        html.Div(id='bothSelectOutput'),
        dash_table.DataTable(data=df.head().to_dict('records'), page_size=10)
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
