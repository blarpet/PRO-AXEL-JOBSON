import dash
import plotly
import dash_core_components as dcc
import dash_html_components as HTML
import plotly_express as px
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


# skapa närvarograd proccent
df = pd.read_csv("National_Total_Deaths_by_Age_Group.csv")



df_AG = df[df["Age_Group"] == "0-9"]
df_AG = df_AG.transpose().iloc[1:]

rlist = [df.Total_Cases, df.Total_ICU_Admissions, df.Total_Deaths]

fig = px.bar(df, x=df.Age_Group, y= rlist, title="Antal fall")

options = []


app.layout = HTML.Div(children=[
    HTML.H1(children="Antal fall"),

    dcc.Dropdown(
    id="drop",
    options=dict(label="Total_Cases", value="Total_Cases")
    ),

    dcc.Graph(
        id="graph",
        figure=fig,
    )
])

@app.callback(
    Output("graph","figure"),
    [Input("drop","value")]
)

def update_figure(value):
    df_AG = df[df["Age_Group"] == value]

    fig = px.bar(df, x=df.Age_Group, y=rlist, title="Antal fall")
    fig.update_layout(transition_duration=500)
    return fig

if __name__ ==  "__main__":
    app.run_server(debug=True)

