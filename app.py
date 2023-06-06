from dash import Dash, dcc, html

from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from src.static.content_intro import contentIntro
from src.static.content_about import contentAbout
from src.dynamic.twod_ex import section2dEx


# Feature tests 1-5
from src.learning.labelled_dropdown_value import labelledDropdownValue
from src.learning.show_simple_plotly_plot import showSimplePlotlyPlot
from src.learning.update_simple_plot_based_on_selection import updateSimplePlotBasedOnSelection
from src.learning.show_simple_3d_plot import showSimple3dPlot
from src.learning.show_clicked_point import showClickedPoint

# Feature tests 6-10
from src.learning.show_lexis_surface_plot import showLexisSurfacePlot
from src.learning.show_hover_click_on_lexis_surface_plot import showHoverClickOnLexisSurfacePlot
from src.learning.show_labelled_countries_generated_from_data import showLabelledcountriesGeneratedFromData
from src.learning.show_sex_country_selection_updated_on_submit_event import showSexCountrySelectionUpdatedOnSubmitEvent
from src.learning.show_can_select_lexis_surface_by_country_and_sex import showLexisSurfaceBasedOnUserCountryAndSexSelection

# Feature tests 11-15
from src.learning.show_lexis_surface_plot_with_subplots import showLexisSurfaceplotWithSubplots
# from src.learning.show_tooltips_on_simple_plot import showTooltipsOnSimplePlot
# from src.learning.show_tooltips_on_3d_plot import showTooltipsOn3dPlot
# from src.learning.show_tooltips_on_options import showTooltipsOnOptions

# Feature tests 16-20

# Feature tests 21-25

# Feature tests 26-30



# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)

app.layout = dbc.Container([
    html.H1('Human Mortality Database Data Visualiser'),
    html.H2('A Python Dash app by Jon Minton'),
    dcc.Tabs(id="tabs-outer", value='tabs-outer-value', children=[
        # dcc.Tab(label="Introduction", value='tab-outer-introduction'),
        # dcc.Tab(label="2D Visualisations", value='tab-outer-2d'),
        # dcc.Tab(label="3D Visualisations", value='tab-outer-3d'),
        dcc.Tab(label='Feature tests 1-5',   value = 'tab-feature-tests_0105'),
        dcc.Tab(label='Feature tests 6-10',  value = 'tab-feature-tests_0610'),
        dcc.Tab(label='Feature tests 11-15', value = 'tab-feature-tests_1115'),
        dcc.Tab(label='Feature tests 16-20',  value = 'tab-feature-tests_1620'),

        # dcc.Tab(label="About", value='tab-outer-about')
    ]),
    html.Div(id='tabs-outer-content')
])

@app.callback(Output('tabs-outer-content', 'children'),
              Input('tabs-outer', 'value'))
def render_outer_content(tab):
    if tab == 'tab-outer-introduction':
        return contentIntro()
    # elif tab == 'tab-outer-2d':
    #     return html.Div([
    #         dcc.Tabs(id='tabs-inner-2d', value='tabs-inner-2d-value', 
    #             children = [
    #                 dcc.Tab(label="Life expectancy", value='tab-ex'),
    #                 dcc.Tab(label="Population sizes", value='tab-pop-N'),                        
    #                 dcc.Tab(label="Age specific mortality", value='tab-mx-over-t'),
    #                 dcc.Tab(label="Sex ratios", value='tab-m_over_f'),
    #             ]         
    #         ),
    #         html.Div(id='tabs-inner-2d-content')
    #     ])
    # elif tab == 'tab-outer-3d':
    #     return html.Div([
    #         dcc.Tabs(id='tabs-inner-3d', value='tabs-inner-3d-value',
    #             children = [
    #                 dcc.Tab(label="Population Structure", value='tab-pop-3d'),
    #                 dcc.Tab(label="Mortality Structure", value='tab-mort-3d'),
    #                 dcc.Tab(label="Sex Ratio Structure", value='tab-mf-3d'),
    #             ]
    #         ),
    #         html.Div(id='tabs-inner-3d-content')
    #     ]
    #     )
    elif tab == 'tab-feature-tests_0105':
        return html.Div([
            dcc.Tabs(id='tabs-inner-featuretests_0105', value = 'tabs-inner-featuretests_0105-value',
                children = [
                    # Feature tests 1-5
                    dcc.Tab(label = 'Labelled Dropdown value', value = 'tab-test-labelledDropdownValue'),
                    dcc.Tab(label = 'Simple Plotly plot', value = 'tab-test-showSimplePlotlyPlot'),
                    dcc.Tab(label = 'Update Simple plot based on user selection', value = 'tab-test-updateSimplePlotBasedOnSelection'),
                    dcc.Tab(label = "Simple 3d plotly plot", value = 'tab-test-showSimple3dPlot'),
                    dcc.Tab(label = "Show clicked point", value = 'tab-test-showClickedPoint'),
                ]     
            ),
            html.Div(id='tabs-inner-featuretests_0105-content')

        ])
    elif tab == 'tab-feature-tests_0610':
        return html.Div([
            dcc.Tabs(id='tabs-inner-featuretests_0610', value = 'tabs-inner-featuretests_0610-value',
                children = [
                    # Feature tests 6-10
                    dcc.Tab(label = "Show Lexis surface plot", value = 'tab-test-showLexisSurfacePlot'),
                    dcc.Tab(label = "Show Lexis surface with hover/click events", value = 'tab-test-showHoverClickLexisSurfacePlot'),
                    dcc.Tab(label = "Show Country selection generated from data", value = 'tab-test-showLabelledCountriesGeneratedFromData'),
                    dcc.Tab(label = "Show country and sex selection updated on submit event", value = 'tab-test-showSexCountrySelectionUpdatedOnSubmitEvent'),
                    dcc.Tab(label = "Show Lexis surface based on user selection of country and sex", value = 'tab-test-showLexisSurfaceBasedOnUserCountryAndSexSelection'),
                    dcc.Tab(label = "Show Lexis surface with subplots", value = 'tab-test-showLexisSurfaceWithSubplots')

                ]
            ),
            html.Div(id='tabs-inner-featuretests_0610-content')
        ])
    elif tab == 'tab-feature-tests-1115':
        return html.Div([
            dcc.Tabs(id='tabs-inner-featuretests_1115', value = 'tabs-inner-featuretests_1115-value',
                children = [
                    # Feature tests 11-15
                    dcc.Tab(label = "Show Lexis surface with subplots", value = 'tab-test-showLexisSurfaceWithSubplots')
                ]         
            ),
            html.Div(id='tabs-inner-featuretests_1115-content')
        ])
    elif tab == 'tab-outer-about':
        return contentAbout()
    

# @app.callback(Output('tabs-inner-2d-content', 'children'),
#               Input('tabs-inner-2d', 'value'))
# def render_inner_2d_content(tab):
#     if tab == 'tab-ex':
#         return section2dEx()
#     elif tab == 'tab-pop-N':
#         return html.Div(
#             html.H4('tab-inner-2d-pop-N')
#         )
#     elif tab == 'tab-m_over_f':
#         return html.Div(
#             html.H4('tab-inner-2d-m_over_f')
#         )
#     elif tab == 'tab-mx-over-t':
#         return html.Div(
#             html.H4('tab-inner-2d-mx-over-t')
#         )
    
@app.callback(Output('tabs-inner-featuretests_0105-content', 'children'),
              Input('tabs-inner-featuretests_0105', 'value'))
def render_featuretests_0105_content(tab):
    # Feature tests 1-5
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
    
@app.callback(Output('tabs-inner-featuretests_0610-content', 'children'),
              Input('tabs-inner-featuretests_0610', 'value'))
def render_featuretests_0610_content(tab):
    # # Feature tests 6-10
    if tab == 'tab-test-showLexisSurfacePlot':
        return showLexisSurfacePlot()
    elif tab == 'tab-test-showHoverClickLexisSurfacePlot':
        return showHoverClickOnLexisSurfacePlot()
    elif tab == 'tab-test-showLabelledCountriesGeneratedFromData':
        return showLabelledcountriesGeneratedFromData()
    elif tab == 'tab-test-showSexCountrySelectionUpdatedOnSubmitEvent':
        return showSexCountrySelectionUpdatedOnSubmitEvent()
    elif tab == 'tab-test-showLexisSurfaceBasedOnUserCountryAndSexSelection':
        return showLexisSurfaceBasedOnUserCountryAndSexSelection()
    if tab == 'tab-test-showLexisSurfaceWithSubplots':
        return showLexisSurfaceplotWithSubplots()

    
@app.callback(Output('tabs-inner-featuretests_1115-content', 'children'),
              Input('tabs-inner-featuretests_1115', 'value'))
def render_featuretests_1115_content(tab):
    # # Feature tests 11-15
    if tab == 'tab-test-showLexisSurfaceWithSubplots':
        return showLexisSurfaceplotWithSubplots()
    else: 
        return None

# @app.callback(Output('tabs-inner-3d-content', 'children'),
#               Input('tabs-inner-3d', 'value'))
# def render_inner_3d_content(tab):
#     if tab == 'tab-pop-3d':
#         return html.Div(
#             html.H4('tab-inner-3d-pop')
#         )
#     elif tab == 'tab-mort-3d':
#         return html.Div(
#             html.H4('tab-inner-3d-mort')
#         )
#     elif tab == 'tab-mf-3d':
#         return html.Div(
#             html.H4('tab-inner-3d-m_over_f')
#         )
      

   

if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1')
