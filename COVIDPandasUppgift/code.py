import pandas as pd #Imports pandas
import matplotlib.pyplot as plt #imports matplotlib.pyplot
import numpy as np #Imports numpy
import plotly.io as pio
import plotly.express as px 
import plotly.graph_objects as go

run = True #sets value of run to true to prepare for the while loop that will loop most of the code
nd = pd.read_csv("National_Daily_Deaths.csv") #Reads in National_Daily_Deaths.csv as nd
nt = pd.read_csv("National_Total_Deaths_by_Age_Group.csv") #Reads in National_Total_Deaths_by_Age_Group.csv as nt
gd = pd.read_csv("Gender_Data.csv")



while run == True: #While true loop
    q1 = str(input("Do you wish to either view National Daily Deaths or the National Total Deaths by Age Group or Gender Data? [NDD/NTDAG/GD/EXIT]")) #Input question
    if q1 == "NDD": #If the answer is NDD it asks another question for which kind of chart of the 2 that you can choose between
        q1_2 = str(input("In which way do you wish to see the data in the chosen CSV file? Line chart or Frequency Diagram? [LC/FD/3DLC]")) #Second Input question
        if q1_2 == "LC": #If the answer is LC then it starts creating a line chart
            plt.title("National Daily Deaths in result of Covid") #Title of line chart
            plt.plot(nd.Date, nd.National_Daily_Deaths, "b.-") #Sets x and y to nd.date and nd.National_Daily_Daths and also sets the color of the line and also adds the dots to the line
            plt.xticks(nd.Date[::75]) #Sets so that the dates wont get to messy so it only shows every 75 days
            plt.xlabel("Day") #Name for X
            plt.ylabel("Casualties") #Name for Y
            plt.show() #Shows line chart
        elif q1_2 == "FD": #If FD is topen in response to th intput it will start to mak a Frequency digram
            bins = [0,10,20,30,40,50,60,70,80,90,100,110,120] #Sets like how many people can die a day so it kind of sums it up to those numbers instead of being like 119 or 121 it goes to 120
            plt.title("Frequency of how many casualties every day has in result of Covid") #Title
            plt.hist(nd.National_Daily_Deaths, bins=bins) #Makes the chart with the nd.National_Daily_Deaths and the bins
            plt.xticks(bins) #Sets so that it ticks from 0 to 10 to 20 and so on until 120
            plt.yticks()
            plt.ylabel("Casualties") #Sets Y name
            plt.show() #Shows diagram
    elif q1 == "NTDAG":
        q1_3 = str(input("In which way do you wish to see the data in the chosen CSV file? Pie chart of Bar chart? [PC/BC/LC]"))
        if q1_3 == "PC":
            labels = ["", "", "", "", "", "50-59", "60-69", "70-79", "80-89", "90+"]
            plt.title("Pie chart of which age groups has the biggest percentage of casualties.")
            def autopctFunction(pct):
                return ('%.2f %%' % pct) if pct > 5 else ''
            plt.pie(nt.Total_Deaths, labels = labels, autopct=autopctFunction)
            plt.show()
        if q1_3 == "BC":
            labels = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90+"]

            convLabels = np.arange(len(labels))
            plt.subplot(2,2,1)
            plt.bar(convLabels, nt.Total_Deaths)
            plt.title("Total deaths for every age group")
            plt.ylabel("Casualties")
            plt.xticks(convLabels, labels)

            plt.subplot(2,2,2)
            plt.bar(convLabels, nt.Total_Cases)
            plt.title(("Total cases for every age group"))
            plt.ylabel("Cases")
            plt.xticks(convLabels, labels)
            plt.show() #Quick tip to widen this to full screen once you open it, it might be different if your screen has a different resolution but who knows, i dont for sure
    elif q1 == "GD":
        q1_4 = str(input("Do you wish to see the gender data in a pie chart? [PC]"))
        if q1_4 == "PC":
            fig = px.pie(gd, values="Total_Cases", names="Gender", title="Total cases of Covid between Genders", color_discrete_sequence=px.colors.sequential.RdBu)
            fig.write_html('first_figure.html', auto_open=True)
    elif q1 == "EXIT":
        run = False
