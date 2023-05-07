from dash import Dash, dcc, html

from dash.dependencies import Input, Output

from src.static.content_intro import contentIntro
from src.static.content_about import contentAbout



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1('Human Mortality Database Data Visualiser'),
    html.H2('A Python Dash app by Jon Minton'),
    dcc.Tabs(id="tabs-outer", value='tabs-outer-value', children=[
        dcc.Tab(label="Introduction", value='tab-outer-introduction'),
        dcc.Tab(label="2D Visualisations", value='tab-outer-2d'),
        dcc.Tab(label="3D Visualisations", value='tab-outer-3d'),
        dcc.Tab(label="About", value='tab-outer-about')
    ]),
    html.Div(id='tabs-outer-content')
])

@app.callback(Output('tabs-outer-content', 'children'),
              Input('tabs-outer', 'value'))
def render_outer_content(tab):
    if tab == 'tab-outer-introduction':
        return contentIntro()
    elif tab == 'tab-outer-2d':
        return html.Div([
            html.H3('tab-outer-2d'),
            dcc.Tabs(id='tabs-inner-2d', value='tabs-inner-2d-value', 
                children = [
                    dcc.Tab(label="Life expectancy", value='tab-ex'),
                    dcc.Tab(label="Population sizes", value='tab-pop-N'),                        
                    dcc.Tab(label="Age specific mortality", value='tab-mx-over-t'),
                    dcc.Tab(label="Sex ratios", value='tab-m_over_f'),
                ]         
            ),
            html.Div(id='tabs-inner-2d-content')
        ]
        )
    elif tab == 'tab-outer-3d':
        return html.Div([
            html.H3('tab-outer-3d'),
            dcc.Tabs(id='tabs-inner-3d', value='tabs-inner-3d-value',
                children = [
                    dcc.Tab(label="Population Structure", value='tab-pop-3d'),
                    dcc.Tab(label="Mortality Structure", value='tab-mort-3d'),
                    dcc.Tab(label="Sex Ratio Structure", value='tab-mf-3d'),
                ]
            ),
            html.Div(id='tabs-inner-3d-content')
        ]
        )
    elif tab == 'tab-outer-about':
        return contentAbout()
    

@app.callback(Output('tabs-inner-2d-content', 'children'),
              Input('tabs-inner-2d', 'value'))
def render_inner_2d_content(tab):
    if tab == 'tab-ex':
        return html.Div(
            html.H4('tab-inner-2d-ex')
        )
    elif tab == 'tab-pop-N':
        return html.Div(
            html.H4('tab-inner-2d-pop-N')
        )
    elif tab == 'tab-m_over_f':
        return html.Div(
            html.H4('tab-inner-2d-m_over_f')
        )
    elif tab == 'tab-mx-over-t':
        return html.Div(
            html.H4('tab-inner-2d-mx-over-t')
        )


@app.callback(Output('tabs-inner-3d-content', 'children'),
              Input('tabs-inner-3d', 'value'))
def render_inner_3d_content(tab):
    if tab == 'tab-pop-3d':
        return html.Div(
            html.H4('tab-inner-3d-pop')
        )
    elif tab == 'tab-mort-3d':
        return html.Div(
            html.H4('tab-inner-3d-mort')
        )
    elif tab == 'tab-mf-3d':
        return html.Div(
            html.H4('tab-inner-3d-m_over_f')
        )

if __name__ == '__main__':
    app.run_server(debug=True)
