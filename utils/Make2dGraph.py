import plotly.graph_objects as go


def make2dGraph(mainTitle, xLabel, yLabel, yLogged, yOrig, xData, yData):

    
    traces = []
    max_y = 0
    for key in yData.keys():
        ySeries = list(yData[key].values())
        if max(ySeries) > max_y:
            max_y = max(ySeries)
        trace = go.Scatter(x = xData, y = ySeries,
                           name = key)
        traces.append(trace)


    if yOrig:
        layout = go.Layout(
            title = mainTitle,
            xaxis_title = xLabel, 
            yaxis = dict(
                title = yLabel,
                type = "log" if yLogged else "linear",
                range = [0, max_y * 1.05]
            )
        )
    else:
        layout = go.Layout(
            title = mainTitle,
            xaxis_title = xLabel, 
            yaxis = dict(
                title = yLabel,
                type = "log" if yLogged else "linear"
            )
        )


    fig = go.Figure(data = traces, layout = layout)
    fig.update_layout(clickmode = 'event+select')


    return fig