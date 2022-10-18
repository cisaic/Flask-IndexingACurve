import numpy as np
import plotly
import plotly.graph_objs as go

import pandas as pd
import json

from hilbert_curve_generator_3D import HilbertCurveGenerator_3D
from hilbert_curve_index_3D import hilbert_index3D


def normalize_value(val, level):
    result = (val * 2 + 1) / (2 ** (level + 1))
    return result


def draw_hilbert3D(dim, level):

    fig = go.Figure()

    hc_seq = pd.read_csv('hilbert-seq-L3.csv')
    hc_seq = hc_seq['seq']

    df = pd.read_csv('hilbert_points.csv')

    fig.add_trace(
        go.Scatter3d(
            x=df['x'],
            y=df['y'],
            z=df['z'],
            name='Hilbert Curve Level: ' + str(level),
            mode='lines',
            text=hc_seq,
            line=dict(
                color=list(range(len(hc_seq))),
                colorscale='Sunset_r',
                width=5),
        )
    )

    fig.layout.plot_bgcolor = 'white'

    camera = dict(
        eye=dict(x=1, y=-1.5, z=.75)
    )

    fig.update_layout(
        scene_camera=camera,
        title="3D Hilbert curve",
        height=500,
        scene=dict(xaxis_showspikes=False,
                   yaxis_showspikes=False,
                   zaxis_showspikes=False,
                   xaxis=dict(range=[0, 1],
                              showbackground=False),
                   yaxis=dict(range=[0, 1],
                              showbackground=False),
                   zaxis=dict(range=[0, 1],
                              showbackground=False))
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON


def step_hilbert3D(dim, level):
    # dim = dimensions of the base plot ex. 2x2x2 starts with 8 quadrants
    # level = level of curve

    # Create figure
    fig = go.Figure()

    hc_gen = HilbertCurveGenerator_3D()
    hc_seq = hc_gen.generate_curve(plot_depth=level)

    coordinates = []
    for seq in hc_seq:
        coordinates.append(hilbert_index3D(seq, [dim, dim, dim]))

    x_vals = [normalize_value(x, level) for [x, y, z] in coordinates]
    y_vals = [normalize_value(y, level) for [x, y, z] in coordinates]
    z_vals = [normalize_value(z, level) for [x, y, z] in coordinates]

    for point in coordinates:
        fig.add_trace(
            go.Scatter3d(
                x=x_vals,
                y=y_vals,
                z=z_vals,
                name='Hilbert Curve Level: ' + str(level),
                mode='lines+markers',
                marker=dict(
                    size=7,
                    color=list(range(len(hc_seq))),
                    colorscale='Viridis'),
                line=dict(
                    color='#677193',
                    width=5),
                visible=False))

    for i, point in enumerate(coordinates):
        # point
        hc_point = point
        x_val = hc_point[0]
        x_val = normalize_value(x_val, level)

        y_val = hc_point[1]
        y_val = normalize_value(y_val, level)

        z_val = hc_point[2]
        z_val = normalize_value(z_val, level)

        fig.add_trace(go.Scatter3d(x=[x_val],
                                   y=[y_val],
                                   z=[z_val],
                                   name='Point corresponding to sequence ' + str(hc_seq[i]),
                                   mode='markers',
                                   visible=False,
                                   marker=dict(
                                       size=10,
                                       color='#e377c2')))
    # Create and add slider
    steps = []

    for i, st in enumerate(fig.data[::2]):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data[::2])},
                  {"title": "3D Hilbert Curve"}],
            label='{}'.format(hc_seq[i]))
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    # Make last trace visible
    fig.data[0].visible = True
    fig.data[len(coordinates)].visible = True

    sliders = [dict(
        active=0,
        currentvalue={"prefix": ""},
        steps=steps
    )]

    camera = dict(
        eye=dict(x=1, y=-1.5, z=.75)
    )

    fig.update_layout(
        scene_camera=camera,
        title="3D Hilbert curve",
        sliders=sliders,
        height=800,
        width=1000,
        scene=dict(xaxis_showspikes=False,
                   yaxis_showspikes=False,
                   zaxis_showspikes=False,
                   xaxis=dict(range=[0, 1], ),
                   yaxis=dict(range=[0, 1], ),
                   zaxis=dict(range=[0, 1], ))
    )

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON
