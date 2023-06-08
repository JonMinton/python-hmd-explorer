import pandas as pd
import numpy as np
from dash import html, dcc, callback
import plotly.graph_objects as go

df = pd.read_csv("assets/data/mx.csv")
d2 = df[
    (df['cntry'] == 'USA') & 
    (df['sex'] == 'female') & 
    (df['age'] <= 90)
]
d2.reset_index(drop = True)

mx_array = d2[
    ['age', 'year', 'mx']
].pivot(
    index = 'year', columns = 'age', values = 'mx'
)
mx_array = np.array(mx_array)

d2['text'] = d2.apply(
    lambda x: "In %s at age %s the %s mortality rate was %1.4f" % (
        x['year'], x['age'], x['sex'], x['mx']
    ), axis = 1
)

text_array = d2[
    ['age', 'year', 'text']
].pivot(
    index = 'year', columns = 'age', values = 'text'
)
text_array = np.array(text_array)


fig = go.Figure(data = [
    go.Surface(
        z = mx_array, text = text_array,
        surfacecolor = np.log(mx_array),
        hovertemplate = '%{text}'
    )
])

fig.update_layout(
    scene = dict(
        zaxis = dict(title = "Logged mortality", type="log"),
        xaxis = dict(title = "Age in years"),
        yaxis = dict(title = "Year")

    )
)



def showCustomTooltipsOnLexisSurface():
    return html.Div([
        html.H4("Show custom hovertext on Lexis surface"),
        html.P("The aim of this feature test is to show custom text on a Lexis surface"),
        dcc.Graph(figure = fig)
    ])