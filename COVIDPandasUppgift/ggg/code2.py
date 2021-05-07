import pandas as pd #Imports pandas
import matplotlib.pyplot as plt #imports matplotlib.pyplot
import numpy as np #Imports numpy
import plotly.io as pio
import plotly.express as px 
import plotly.graph_objects as go


nd = pd.read_csv("National_Daily_Deaths.csv")
nt = pd.read_csv("National_Total_Deaths_by_Age_Group.csv")
gd = pd.read_csv("Gender_Data.csv")

fig = px.line(nt, x="Age_Group", y="Total_Cases", labels={"x": "Age groups", "y" : "Total Cases"})
fig = px.line(nt, x="Age_Group", y="Total_ICU_Admissions", labels={"x": "Age groups", "y" : "Total ICU Admissions"})
fig = px.line(nt, x="Age_Group", y="Total_Deaths", labels={"x": "Age groups", "y" : ["Total Cases", "Total Deaths, Total ICU Admissions"]})
fig.write_html('first_figure.html', auto_open=True)
