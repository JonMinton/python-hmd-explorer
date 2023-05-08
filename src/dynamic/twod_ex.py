from dash import html, dcc, Dash, Input, Output, callback

def section2dEx():
    return html.Div([
        html.H4('tab-inner-2d-ex IN MODULE'),
        dcc.Dropdown([
            {'label': "Male", 'value': 'male'}, 
            {'label': "Female", 'value': 'female'},
            {'label': 'Total', 'value': 'total'},
        ], 
        'total', 
        id='sex-select'
        ),
        html.Div(id='sex-select-output')
    ])




@callback(
    Output('sex-select-output', 'children'),
    Input('sex-select', 'value')
)
def update_output(value):
    return f'You have selected {value}'
