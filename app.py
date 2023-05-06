from dash import Dash, dcc, html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Dash Tabs component demo'),
    dcc.Tabs(id="tabs-example-graph", value='tab-1-example-graph', children=[
        dcc.Tab(label="Introduction", value='tab-intro'),
        dcc.Tab(label='Life Expectancies', value='tab-ex'),
        dcc.Tab(label='Age specific Mortality', value='tab-mort-2d'),
        dcc.Tab(label='Population Sizes', value='tab-pop-2d'),
        dcc.Tab(label='Mortality', value='tab-mort-3d'),
        dcc.Tab(label='Population', value='tab-pop-3d'),
        dcc.Tab(label="About", value='tab-about')

    ]),
    html.Div(id='tabs-content-example-graph')
])

@app.callback(Output('tabs-content-example-graph', 'children'),
              Input('tabs-example-graph', 'value'))
def render_content(tab):
    if tab == 'tab-intro':
        return html.Div(
            html.H3("tab-intro")
        )
    elif tab == 'tab-ex':
        return html.Div(
            html.H3('tab-ex')
        )
    elif tab == 'tab-mort-2d':
        return html.Div(
            html.H3('tab-mort-2d')
        )
    elif tab == 'tab-pop-2d':
        return html.Div(
            html.H3('tab-pop-2d')
        ) 
    elif tab == 'tab-mort-3d':
        return html.Div(
            html.H3('tab-mort-3d')
        )
    elif tab == 'tab-pop-3d': 
        return html.Div(
            html.H3('tab-pop-3d')
        )
    elif tab == 'tab-about':
        return html.Div(
            html.H3('tab-about')
        )

if __name__ == '__main__':
    app.run_server(debug=True)
