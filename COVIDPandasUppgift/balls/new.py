import pandas as pd
import plotly.express as px

df = pd.read_csv("National_Total_Deaths_by_Age_Group.csv")
options = []

for age in df.Age_Group:
    options.append(dict(label = age, value = age))

fig = px.bar(df,x = "Age_Group", y = "Total_Cases")
fig.write_html('first_figure.html', auto_open=True)
print(df.head())
#df_AG = df[df["Age_Group"] == "0-9"]
#df_AG = df_AG.transpose().iloc[1:]
#print(df_AG)

