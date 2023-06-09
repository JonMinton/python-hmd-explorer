import pandas as pd
import plotly.express as px


def canvas2dLifetables(place_value, sex_value):
    dta = pd.read_csv("assets/data/lifetables.csv")
    adj_sex_value = "both" if sex_value == "total" else sex_value
    d2 = dta.loc[
        (dta['cntry'] == place_value) & 
        (dta['sex'] == adj_sex_value) & 
        (dta['age'] == 0), :
    ]

    fig = px.line(d2, x= 'year', y = 'ex')
    return fig    