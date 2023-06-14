import plotly.graph_objects as go
import numpy as np

def make3dLexisSurface(lsType, xTitle, yTitle, zTitle, mainTitle, xSeries, ySeries, zArray, logZ, colorscale):
    print("In make3dLexisSurface")
    print(f"colorscale passed is {colorscale}")
    if lsType == '3d':
        fig = go.Figure(
            data = 
            [go.Surface(
                x = xSeries,
                y = ySeries,
                z = zArray,
                surfacecolor = np.log(zArray) if logZ else zArray,
                colorscale = colorscale
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
        fig.update_layout(
            margin = dict(
                pad = 0,
                l = 0,
                r = 0,
                t = 0, 
                b = 0
            )
        )
        return fig
    elif lsType == 'contour-heatmap':
        fig = go.Figure(
            data = 
            [go.Contour(
            # For contour map should swap axes
                y = xSeries,
                x = ySeries,
                z = np.log(np.transpose(zArray)) if logZ else np.transpose(zArray),
                colorscale = colorscale
            )]
        )
        fig.update_layout(
            title = mainTitle, 
            xaxis_title = xTitle,
            yaxis_title = yTitle
        )
        fig.update_layout(
            margin = dict(
                pad = 0,
                l = 0,
                r = 0,
                t = 0, 
                b = 0
            )
        )

        return fig
    elif lsType == 'heatmap-only':
        fig = go.Figure(
            data = 
            [go.Heatmap(
                # swap and transpose 
                y = xSeries,
                x = ySeries,
                z = np.log(np.transpose(zArray)) if logZ else np.transpose(zArray),
                colorscale = colorscale
            )]
        )
        fig.update_layout(
            title = mainTitle, 
            xaxis_title = xTitle,
            yaxis_title = yTitle
        )
        fig.update_layout(
            margin = dict(
                pad = 0,
                l = 0,
                r = 0,
                t = 0, 
                b = 0
            )
        )

        return fig
    else: 
        return None