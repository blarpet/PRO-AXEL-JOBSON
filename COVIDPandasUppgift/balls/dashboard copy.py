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
TE19 = np.random.randint(50,100,29)
NA19 = np.random.randint(20,100,25)

df_TE19 = pd.DataFrame(dict(Närvarograd=TE19))
df_NA19 = pd.DataFrame(dict(Närvarograd=NA19))

fig = px.bar(df_NA19, y="Närvarograd", title="Närvarograd för olika klasser")

app.layout = HTML.Div(children=[
    HTML.H1(children="Närvarograd för olika klasser"),

    dcc.Dropdown(
    id="drop",
    options=[dict(label="TE19", value="TE19"),
             dict(label="NA19", value="NA19")]
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
    if value == "TE19": df = df_TE19
    elif value == "NA19": df = df_NA19

    fig = px.bar(df, y="Närvarograd", title=f"Närvarograd i procent för {value}")
    fig.update_layout(transition_duration=500)
    return fig

if __name__ ==  "__main__":
    app.run_server(debug=True)
