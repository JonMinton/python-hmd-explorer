import plotly.graph_objects as go
import numpy as np

def make3dLexisSurface(lsType, xTitle, yTitle, zTitle, mainTitle, xSeries, ySeries, zArray, logZ):
    
    if lsType == '3d':
        fig = go.Figure(
            data = 
            [go.Surface(
                x = xSeries,
                y = ySeries,
                z = zArray,
                surfacecolor = np.log(zArray) if logZ else zArray
            )]
        )
        fig.update_layout(
            title = mainTitle, 
            scene = dict(
                zaxis = dict(
                    title = zTitle, 
                    type = "log" if logZ else "linear"             
                ),
                xaxis = dict(title = xTitle),
                yaxis = dict(title = yTitle)
            )
        )
        return fig
    elif lsType == 'contour-heatmap':
        fig = go.Figure(
            data = 
            [go.Contour(
                x = xSeries,
                y = ySeries,
                z = zArray
            )]
        )
        fig.update_layout(
            title = mainTitle, 
            xaxis_title = xTitle,
            yaxis_title = yTitle
        )
        return fig
    elif lsType == 'heatmap-only':
        fig = go.Figure(
            data = 
            [go.Heatmap(
                x = xSeries,
                y = ySeries,
                z = zArray
            )]
        )
        fig.update_layout(
            title = mainTitle, 
            xaxis_title = xTitle,
            yaxis_title = yTitle
        )
        return fig
    else: 
        return None