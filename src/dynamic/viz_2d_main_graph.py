import plotly.express as px
import plotly.graph_objects as go
from dash import dcc

def viz2dMainGraph(mainTitle, xLabel, yLabel, yLogged, xData, yData):

    data = go.Scatter(x = xData, y = yData)
    layout = go.Layout(
        title = mainTitle,
        xaxis_title = xLabel, 
        yaxis_title = yLabel
        )
    fig = go.Figure(data = data, layout = layout)

    return dcc.Graph(figure = fig)