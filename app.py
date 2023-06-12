import dash
from dash import Dash, dcc, html

from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from src.style_wrappers.navitem_wrapper import makeNavItem




# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], 
           suppress_callback_exceptions=True ,
           use_pages=True
           )




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
                        style = {
                            "text-align" : "center"
                            }
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
            # dcc.Tab(label="3D Visualisations", value='tab-outer-3d', className = "nav-item mt-1"),
            dcc.Tab(label="About", value='tab-outer-about', className = "nav-item mt-1")
        ],
        className = "nav nav-tabs mb-3"
    ),
    dcc.Location(id = 'location'),

    dash.page_container
    ],
    fluid=False, # True removes margins from either side of the container
    style = {
        "height": "100vh",
        "display" : "flex",
        "flex-direction" : "column"
    }
    )

@app.callback(Output('location', 'href'),
              Input('tabs-outer', 'value'))
def render_outer_content(tab):
    # dash.page_container
    if tab == 'tab-outer-introduction':
        return '/'
        # return contentIntro()
    elif tab == 'tab-outer-2d':
        return '/2d'
    # elif tab == 'tab-outer-3d':
    #     return layout3dVisualisation()
    elif tab == 'tab-outer-about':
        return '/about'
        # return contentAbout()
    


if __name__ == '__main__':
    app.run_server(debug=True, host = '127.0.0.1')
