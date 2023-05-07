from dash import html, dcc

def contentIntro():
    return dcc.Markdown('''
        ### New intro content in markdown format

        This is some standard text
    
    ''')