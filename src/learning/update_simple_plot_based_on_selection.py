# Aim of this snippet

# Update a simple plotly plot based on user selection 

from dash import html, dcc, Input, Output, callback
import plotly.express as px

df = px.data.iris()  # iris is a pandas DataFrame
fig = px.scatter(
    df,
    x = "sepal_width",
    y = "sepal_length"
)

df_unique_combinations = df[['species', 'species_id']].drop_duplicates()

lab_values_for_dropdown = []
for index, row in df_unique_combinations.iterrows():
    modified_dict = {'label': row['species'], 'value': row['species_id']}
    lab_values_for_dropdown.append(modified_dict)



def updateSimplePlotBasedOnSelection():
    return html.Div([
        html.H4("Update plot based on user selection"),
        html.P("The aim of this feature test is to update the displayed graph based on user selection"),
        dcc.Graph(id = "selection-updated-scatterplot", figure = fig),
        dcc.Dropdown(
            options = lab_values_for_dropdown,
            value = 2,
            id = 'labelled-dropdown2'
        ),
        html.Div(id='simpleplot-option-output-container')
    ])

@callback(
    Output('simpleplot-option-output-container', 'children'),
    Input('labelled-dropdown2', 'value')
)
def updateOutput(value):
    return f'You selected {value}'

@callback(
    Output("selection-updated-scatterplot", component_property="figure"),
    [Input("labelled-dropdown2", "value")]
)
def updateFigure(species_id):
    print(f'value selected by user: {species_id}')

    def is_selected(row):
        if row['species_id'] == species_id:
            return True
        else:
            return False

    if species_id == None:
        fig = {}
    else:
        df['selected'] = df.apply(is_selected, axis = 1)
        fig = px.scatter(
            df,
            x = "sepal_width",
            y = "sepal_length",
            color = "selected"
        )
        fig.update_layout();
    return fig
