import pandas as pd
import plotly.express as px


def canvas2dExposures(place_value, sex_value):
    dta = pd.read_csv("assets/data/exposures.csv")
    d2  = dta.loc[
        (dta['cntry'] == place_value) & 
        (dta['sex'] == sex_value), :
    ]
    d3 = d2.groupby(['year']).agg({"exposures_count" : "sum"}).reset_index()

    fig = px.line(d3, x = "year", y = "exposures_count")
    return fig    