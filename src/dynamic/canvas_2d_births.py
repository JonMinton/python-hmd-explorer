import pandas as pd
import plotly.express as px


def canvas2dBirths(place_value, sex_value):
    dta = pd.read_csv("assets/data/births.csv")
    d2 = dta.loc[
        (dta['cntry'] == place_value) & 
        (dta['sex'] == sex_value), :
    ]
    fig = px.line(d2, x="year", y="number_of_births")
    return fig    