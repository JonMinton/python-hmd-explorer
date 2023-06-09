import pandas as pd
import plotly.express as px


def canvas2dDeaths(place_value, sex_value):
    dta = pd.read_csv("assets/data/deaths.csv")
    d2 = dta.loc[
        (dta['cntry'] == place_value) & 
        (dta['sex'] == sex_value)
    ]
    # The code below returns the total number of deaths by year
    d3 = d2.groupby(['year']).agg({"number_of_deaths" : "sum"}).reset_index()
    
    fig = px.line(d3, x = "year", y = "number_of_deaths")
    return fig    