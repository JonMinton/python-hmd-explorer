from dash import Dash, dcc, html

from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from src.style_wrappers.navitem_wrapper import makeNavItem

from src.static.content_intro import contentIntro
from src.static.content_about import contentAbout
from src.layouts.layout_2d_visualisation import layout2dVisualisation
from src.layouts.layout_3d_visualisation import layout3dVisualisation



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
from src.learning.show_custom_tooltips_on_simple_plot import showCustomTooltipsOnSimplePlot
from src.learning.show_custom_tooltips_on_lexis_surface import showCustomTooltipsOnLexisSurface
from src.learning.show_can_use_dbc import showCanUseDbc

# Feature tests 16-20

# Feature tests 21-25

# Feature tests 26-30



# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], suppress_callback_exceptions=True)




app.layout = dbc.Container([
    dbc.Row(
        [
            dbc.Col(
                dbc.Nav(
                    dbc.Navbar(
                        [
                            makeNavItem("bi bi-database", "Data", "https://www.mortality.org/Data/DataAvailability"),
                            makeNavItem("bi bi-app", "HMD", "https://www.mortality.org/Home/Index"),
                            makeNavItem("bi bi-journal-album", "Methods", "https://www.mortality.org/File/GetDocument/Public/Docs/MethodsProtocolV6.pdf"),
                            makeNavItem("bi bi-journal-code", "API", "https://cran.r-project.org/web/packages/HMDHFDplus/index.html")

                        ]
                    )
                ),
                width = 3
            ),
            dbc.Col(
                    html.H1(
                        'Demographic Data Visualiser',
                        style = {"text-align" : "center"}
                    ),
                width = 6
            ),
            dbc.Col(
                dbc.Nav(
                    dbc.Navbar(
                        children = [
                            makeNavItem("bi bi-github", "Repo", "https://github.com/jonminton/python-hmd-explorer"),
                            makeNavItem("bi bi-linkedin", "LinkedIn", "https://www.linkedin.com/in/jon-minton-09480b13a/?originalSubdomain=uk"),
                            makeNavItem("bi bi-github", "Repos", "https://github.com/JonMinton"), 
                            makeNavItem("bi bi-twitter", "Twitter", "https://twitter.com/jonminton")

                        ]
                    )
                ),

                width = 3
            )
        ],
       style = {"margin-bottom": "0.5rem"},
       className = ("g-0")
    ),
    dcc.Tabs(
        id="tabs-outer", value='tabs-outer-value', 
        children=[
            dcc.Tab(label="Introduction", value='tab-outer-introduction', className = "nav-item mt-1"),
            dcc.Tab(label="2D Visualisations", value='tab-outer-2d', className = "nav-item mt-1"),
            dcc.Tab(label="3D Visualisations", value='tab-outer-3d', className = "nav-item mt-1"),
        # dcc.Tab(label='Feature tests 1-5',   value = 'tab-feature-tests_0105'),
        # dcc.Tab(label='Feature tests 6-10',  value = 'tab-feature-tests_0610'),
        # dcc.Tab(label='Feature tests 11-15', value = 'tab-feature-tests_1115'),
        # dcc.Tab(label='Feature tests 16-20',  value = 'tab-feature-tests_1620'),

            dcc.Tab(label="About", value='tab-outer-about', className = "nav-item mt-1")
        ],
        className = "nav nav-tabs mb-3"
    ),
    html.Div(
        id='tabs-outer-content',
        style = {
            "height" : "100%"
        },
        className = "mb-3"
    )
    ],
    fluid=False, # True removes margins from either side of the container
    style = {
        "height": "100vh",
        "display" : "flex",
        "flex-direction" : "column"
    }
    )

@app.callback(Output('tabs-outer-content', 'children'),
              Input('tabs-outer', 'value'))
def render_outer_content(tab):
    if tab == 'tab-outer-introduction':
        return contentIntro()
    elif tab == 'tab-outer-2d':
        return layout2dVisualisation()
    elif tab == 'tab-outer-3d':
        return layout3dVisualisation()
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
    elif tab == 'tab-feature-tests_1115':
        return html.Div([
            dcc.Tabs(id='tabs-inner-featuretests_1115', value = 'tabs-inner-featuretests_1115-value',
                children = [
                    # Feature tests 11-15
                    dcc.Tab(label = "Show Lexis surface with subplots", value = 'tab-test-showLexisSurfaceWithSubplots'),
                    dcc.Tab(label = "Show custom tooltips on simple plot", value = 'tab-test-showCustomTooltipsOnSimplePlot'),
                    dcc.Tab(label = "Show custom tooltips on Lexis surface", value = "tab-test-showCustomTooltipsOnLexisSurface"),
                    dcc.Tab(label = "Show bootstrap components 1", value = "tab-test-showBoostrapComponents1")
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
    elif tab == 'tab-test-showCustomTooltipsOnSimplePlot':
        return showCustomTooltipsOnSimplePlot()
    elif tab == "tab-test-showCustomTooltipsOnLexisSurface":
        return showCustomTooltipsOnLexisSurface()
    elif tab == "tab-test-showBoostrapComponents1":
        print("called!")
        return showCanUseDbc()
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
