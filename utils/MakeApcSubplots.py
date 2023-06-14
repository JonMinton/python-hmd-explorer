import plotly.graph_objects as go
import plotly.subplots as sp

def makeApcSubplots(arrangement, dAge, dPeriod, dCohort, logZ):

    if arrangement == 'col':
        subfigs = sp.make_subplots(rows = 3, cols = 1)

        subfigs.add_trace(
            go.Line(x = dAge['year'], y = dAge.iloc[:,1]),
            row = 1, col = 1
        )
        subfigs.add_trace(
            go.Line(x = dPeriod['age'], y = dPeriod.iloc[:,1]),
            row = 2, col = 1
        )
        subfigs.add_trace(
            go.Line(x = dCohort['age'], y = dCohort.iloc[:,1]),
            row = 3, col = 1
        )

        subfigs.update_xaxes(title_text = "Year", row = 1, col = 1)
        subfigs.update_xaxes(title_text = "Age in Years", row = 2, col = 1)
        subfigs.update_xaxes(title_text = "Age in Years", row = 3, col = 1)

        if logZ:
            subfigs.update_yaxes(
                type = 'log',
                row = 1, col = 1
            )
            subfigs.update_yaxes(
                type = 'log',
                row = 2, col = 1
            )
            subfigs.update_yaxes(
                type = 'log',
                row = 3, col = 1
            )

        
    elif arrangement == 'row':
        subfigs = sp.make_subplots(rows = 1, cols = 3)

        subfigs.add_trace(
            go.Line(x = dAge['year'], y = dAge.iloc[:,1]),
            row = 1, col = 1
        )
        subfigs.add_trace(
            go.Line(x = dPeriod['age'], y = dPeriod.iloc[:,1]),
            row = 1, col = 2
        )
        subfigs.add_trace(
            go.Line(x = dCohort['age'], y = dCohort.iloc[:,1]),
            row = 1, col = 3
        )


        subfigs.update_xaxes(title_text = "Year", row = 1, col = 1)
        subfigs.update_xaxes(title_text = "Age in Years", row = 1, col = 2)
        subfigs.update_xaxes(title_text = "Age in Years", row = 1, col = 3)

        if logZ:
            subfigs.update_yaxes(
                type = 'log',
                row = 1, col = 1
            )
            subfigs.update_yaxes(
                type = 'log',
                row = 1, col = 2
            )
            subfigs.update_yaxes(
                type = 'log',
                row = 1, col = 3
            )

    subfigs.update_layout(showlegend=False)
    subfigs.update_layout(
        margin = dict(
            pad = 0,
            l = 0,
            r = 0,
            t = 0, 
            b = 0
        )
    )

    return subfigs
    