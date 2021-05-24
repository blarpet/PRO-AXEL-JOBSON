#Imports a bunch of modules v
import dash
import plotly 
import dash_core_components as dcc
import dash_html_components as HTML
import plotly_express as px
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

#Note: If you try to run this code it could be a bit annoying because what could happen is that code.py
#might run instead even if its not open and you havent even pressed the run button on code.py
#to fix this temporarly put code.py somewhere else like in another folder, that seemed to work for me atleast


df = pd.read_csv("National_Total_Deaths_by_Age_Group.csv")



df_AG = df[df["Age_Group"] == "0-9"]
df_AG = df_AG.transpose().iloc[1:]


#List for the things to be shown in the bar chart
rlist = [df.Total_Cases, df.Total_ICU_Admissions, df.Total_Deaths]

fig = px.bar(df, x=df.Age_Group, y= rlist, title="Antal fall")

options = []

#Layout for the html like the dropdown feature which i didnt use
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
#updates it if you use the dropdown feature which again i didnt use
def update_figure(value):
    df_AG = df[df["Age_Group"] == value]
    #Makes the whole bar chart and all that
    fig = px.bar(df, x=df.Age_Group, y=rlist, title="Antal fall")
    fig.update_layout(transition_duration=500)
    return fig

if __name__ ==  "__main__":
    app.run_server(debug=True)

