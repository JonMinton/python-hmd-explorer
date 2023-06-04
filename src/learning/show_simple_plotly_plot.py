# Aim of this snippet

# Show a simple 2d plotly plot of one value against another

from dash import html, dcc
import plotly.express as px

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")



def showSimplePlotlyPlot():
    return html.Div([
        html.H4("Show simple plotly plot"),
        html.P("The aim of this feature test is to show a simple plotly plot"),
        dcc.Graph(figure=fig)

    ])