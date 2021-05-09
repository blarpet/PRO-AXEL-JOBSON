import pandas as pd 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np

np.random.seed(2020)

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id="graph")
])


def display_color(std):
    data = np.random.normal(std, size=500)
    fig = px.histogram(data, nbins=30, range_x=[-10, 10])
    return fig

app.run_server(debug=True)