import plotly.graph_objects as go

def make2dDifferenceGraph(mainTitle, xLabel, yLabel, xData, yData):
    print("in make2dDifferenceGraph")
    # print(xData)
    # print(yData)
    print(f"xData before popping is length {len(xData)}")
    print(f"type of xData is {type(xData)}")
    xData.pop() #To remove last year
    print(f"xData after popping is length {len(xData)}")
    traces = [] 
    max_y = 0
    for key in yData.keys():
        ySeries = list(yData[key].values())
        absYSeries = [abs(y) for y in ySeries]
        print(ySeries)
        print(len(ySeries))
        print(len(xData))
        if max(absYSeries) > max_y:
            max_y = max(absYSeries) #absolute as negatives as important as positives
            print(f"max_y updated to {max_y}")
        print(f"xData is {len(xData)} long and ySeries is {len(ySeries)} long")
        trace = go.Scatter(x = xData, y = ySeries, name = key)
        traces.append(trace)
    print(len(traces))
    layout = go.Layout(
        title  = mainTitle, 
        xaxis_title = xLabel, 
        yaxis = dict(
            title = yLabel,
            range = [-max_y * 1.05, max_y * 1.05] #symmetric around absolutes
        )
    )

    fig = go.Figure(data = traces, layout = layout)
    fig.update_layout(clickmode = 'event+select')

    return fig