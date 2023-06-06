from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd
import numpy as np

df = pd.read_csv("assets/data/mx.csv")
df_ss = df[
    (df['cntry'] == 'USA') & 
    (df['sex'] == 'female') & 
    (df['age'] <= 90)
]
df_ss.reset_index(drop = True)

mx_array = df_ss[
    ['age', 'year', 'mx']
].pivot(
    index = 'year', columns = 'age', values = 'mx'
)
mx_array = np.array(mx_array)

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

def showLexisSurfacePlot():
    return html.Div([
        html.H4('Show Lexis Surface Plot'),
        html.P("The aim of this feature test is to confirm I can create a 3d surface plot of a downloaded population"),
        dcc.Graph(figure = fig)

    ])
