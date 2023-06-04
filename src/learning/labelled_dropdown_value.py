# Aim of this snippet

# Create a dropdown menu with the following options and labels

# {'Male': 'male'}
# {'Female' : 'female'}
# {'Total' : 'total}

#(i.e. the labels start with uppercase, the values are all lowercase)


# show the VALUE of the option selected.
# confirm that on initialisation the 'male' value is shown

from dash import html, Dash, dcc, Input, Output, callback

def labelledDropdownValue():
    return html.Div([
        html.H4("Labelled Dropdown Test"),
        html.P("The aim of this feature test is to produce a dropdown menu with three options. Each option will have a label, which is slightly different to the label. The value, not the label, should be passed to an output. Initally a default value should be passed to the output"),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montreal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'},
            ],
            value='MTL',
            id = 'labelled-dropdown'
        ),
        html.Div(id='option-output-container')
    ])


# app.layout = html.Div([
#     dcc.Dropdown(['NYC', 'MTL', 'SF'], 'NYC', id='demo-dropdown'),
#     html.Div(id='dd-output-container')
# ])


@callback(
    Output('option-output-container', 'children'),
    Input('labelled-dropdown', 'value')
)
def update_output(value):
    return f'You have selected {value}'


# if __name__ == '__main__':
#     app.run_server(debug=True)

# dcc.Dropdown(
#    options=[
#        {'label': 'New York City', 'value': 'NYC'},
#        {'label': 'Montreal', 'value': 'MTL'},
#        {'label': 'San Francisco', 'value': 'SF'},
#    ],
#    value='MTL'
# )