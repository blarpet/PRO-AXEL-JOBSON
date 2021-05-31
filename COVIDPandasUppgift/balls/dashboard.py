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
#TE19 = np.random.randint(50,100,29)
#NA19 = np.random.randint(20,100,25)



#df_TE19 = pd.DataFrame(dict(Närvarograd=TE19))
#df_NA19 = pd.DataFrame(dict(Närvarograd=NA19))
df_AG = df[df["Age_Group"] == "0-9"]
df_AG = df_AG.transpose().iloc[1:]

fig = px.bar(df_AG, y= ["0"], title="Närvarograd för olika klasser")

options = []

for age in df.Age_Group:
    options.append(dict(label = age, value = age))


app.layout = HTML.Div(children=[
    HTML.H1(children="Närvarograd för olika klasser"),

    dcc.Dropdown(
    id="drop",
    options=options, value="0-9"
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

    fig = px.bar(df_AG, title=f"Närvarograd i procent för {value}")
    fig.update_layout(transition_duration=500)
    return fig

if __name__ ==  "__main__":
    app.run_server(debug=True)