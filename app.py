from dash import Dash, dcc, html

from dash.dependencies import Input, Output

import pickle

from src.static.content_intro import contentIntro
from src.static.content_about import contentAbout

from src.dynamic.twod_ex import section2dEx


from src.learning.labelled_dropdown_value import labelledDropdownValue
from src.learning.show_simple_plotly_plot import showSimplePlotlyPlot
from src.learning.update_simple_plot_based_on_selection import updateSimplePlotBasedOnSelection
from src.learning.show_simple_3d_plot import showSimple3dPlot
from src.learning.show_clicked_point import showClickedPoint

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.H1('Human Mortality Database Data Visualiser'),
    html.H2('A Python Dash app by Jon Minton'),
    dcc.Tabs(id="tabs-outer", value='tabs-outer-value', children=[
        dcc.Tab(label="Introduction", value='tab-outer-introduction'),
        dcc.Tab(label="2D Visualisations", value='tab-outer-2d'),
        dcc.Tab(label="3D Visualisations", value='tab-outer-3d'),
        dcc.Tab(label='Feature tests', value = 'tab-feature-tests'),
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
        ])
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
    elif tab == 'tab-feature-tests':
        return html.Div([
            html.H3('Feature tests'),
            dcc.Tabs(id='tabs-inner-featuretests', value = 'tabs-inner-featuretests-value',
                children = [
                    dcc.Tab(label = 'Labelled Dropdown value', value = 'tab-test-labelledDropdownValue'),
                    dcc.Tab(label = 'Simple Plotly plot', value = 'tab-test-showSimplePlotlyPlot'),
                    dcc.Tab(label = 'Update Simple plot based on user selection', value = 'tab-test-updateSimplePlotBasedOnSelection'),
                    dcc.Tab(label = "Simple 3d plotly plot", value = 'tab-test-showSimple3dPlot'),
                    dcc.Tab(label = "Show clicked point", value = 'tab-test-showClickedPoint')
                ]     
            ),
            html.Div(id='tabs-inner-featuretests-content')

        ])
    elif tab == 'tab-outer-about':
        return contentAbout()
    

@app.callback(Output('tabs-inner-2d-content', 'children'),
              Input('tabs-inner-2d', 'value'))
def render_inner_2d_content(tab):
    if tab == 'tab-ex':
        return section2dEx()
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
    
@app.callback(Output('tabs-inner-featuretests-content', 'children'),
              Input('tabs-inner-featuretests', 'value'))
def render_featuretests_content(tab):
    if tab == 'tab-test-labelledDropdownValue':
        return labelledDropdownValue()
    elif tab == 'tab-test-showSimplePlotlyPlot':
        return showSimplePlotlyPlot()
    elif tab == 'tab-test-updateSimplePlotBasedOnSelection':
        return updateSimplePlotBasedOnSelection()
    elif tab == 'tab-test-showSimple3dPlot':
        return showSimple3dPlot()
    elif tab == 'tab-test-showClickedPoint':
        return showClickedPoint()


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
    app.run_server(debug=True, host = '127.0.0.1')
