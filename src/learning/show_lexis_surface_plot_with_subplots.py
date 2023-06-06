from dash import html, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import plotly.express as px
import plotly.subplots as sp
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
        x = np.arange(df_ss['age'].min(), df_ss['age'].max()),
        y = np.arange(df_ss['year'].min(), df_ss['year'].max()),
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

# Let's start with a default age, period and cohort schedule to 
# confirm that that works


def showLexisSurfaceplotWithSubplots():
    return dbc.Row(
        [
            dbc.Row(
                dbc.Col(
                    [
                        html.H4("Lexis surface with subplots"),
                        html.P("""
                            The aim of this feature test is to show a Lexis surface which, 
                            when a point on the surface is clicked on, generates three subplots containing
                            the age, period and birth cohort schedules that intersect at that point
                        """)
                    ],
                    width = 12
                ),
                justify="start"   
            ),
            dbc.Row(    
                [
                dbc.Col(
                    [
                        dcc.Graph(id = "clickable-lexis-surface-for-subplots", figure = fig),
                    ],
                    width = 4
                ),
                dbc.Col(
                    [
                        dcc.Graph(id = 'subfig-age'),
                        dcc.Graph(id = 'subfig-period'),
                        dcc.Graph(id = 'subfig-cohort')
                    ],
                    width = 5
                )
                ],
                justify = 'start'
            )
        ]
    )     




# # @callback(
# #     Output('click-data-lexis-subplots', 'children'),
# #     Input('clickable-lexis-surface-for-subplots', 'clickData')
# # )
# # def display_click_data(clickData):
# #     if clickData is not None:
# #         return 'Clicked: x={}, y={}, z={}'.format(
# #             clickData['points'][0]['x'],
# #             clickData['points'][0]['y'],
# #             clickData['points'][0]['z']
# #         )

@callback(
    Output('subfig-age', component_property = 'figure'),
    [Input('clickable-lexis-surface-for-subplots', 'clickData')]
)
def updateAgeSubplot(clickData):
    if clickData is None:
        figAge = {}
    else:
        selectedAge = clickData['points'][0]['x']

        df_ssSelectedAge = df_ss[(df_ss['age'] == selectedAge)]
        figAge = px.line(df_ssSelectedAge, x = 'year', y = 'mx', log_y=True)

    return figAge

@callback(
    Output('subfig-period', component_property = 'figure'),
    [Input('clickable-lexis-surface-for-subplots', 'clickData')]
)
def updatePeriodSubplot(clickData):
    if clickData is None:
        figPeriod = {}
    else:
        selectedPeriod = clickData['points'][0]['y']

        df_ssSelectedPeriod = df_ss[(df_ss['year'] == selectedPeriod)]
        figPeriod = px.line(df_ssSelectedPeriod, x = 'age', y = 'mx', log_y=True)

    return figPeriod

@callback(    
    Output('subfig-cohort', component_property = 'figure'),
    [Input('clickable-lexis-surface-for-subplots', 'clickData')]
)
def updateCohortSubplot(clickData):
    if clickData is None:
        figCohort = {}
    else:
        selectedAge = clickData['points'][0]['x']
        selectedPeriod = clickData['points'][0]['y']
        selectedCohort = selectedPeriod - selectedAge

        df_ssSelectedCohort = df_ss.loc[(df_ss['year'] - df_ss['age'])== selectedCohort, :]
        figCohort = px.line(df_ssSelectedCohort, x = 'age', y = 'mx', log_y = True)
    return figCohort
