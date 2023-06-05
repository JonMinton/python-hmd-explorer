from dash import html, dcc
import plotly.express as px
import pandas as pd


usaFemPop = pd.read_csv("assets/data/population.csv")
useFemPop.fi[cntry == "USA"]
print(usaFemPop.head(6))

def showLexisSurfacePlot():
    return html.Div([
        html.H4('Show Lexis Surface Plot'),
        html.P("The aim of this feature test is to confirm I can create a 3d surface plot of a downloaded population")
        

    ])
