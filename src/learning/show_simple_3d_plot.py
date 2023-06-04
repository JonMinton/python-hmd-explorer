from dash import html, dcc
import plotly.express as px

df = px.data.iris()

fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')

def showSimple3dPlot():
    return html.Div([
        html.H4('Show simple 3d plot'),
        html.P("The aim of this feature test is to show a simple 3d plotly plot"),
        dcc.Graph(figure = fig)

    ])
