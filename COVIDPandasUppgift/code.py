import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
run = True

nd = pd.read_csv("National_Daily_Deaths.csv")
nt = pd.read_csv("National_Total_Deaths_by_Age_Group.csv") 



while run == True:
    q1 = str(input("Do you wish to either view National Daily Deaths or the National Total Deaths by Age Group? [NDD/NTDAG/NEITHER]"))
    if q1 == "NDD":
        q1_2 = str(input("Do you wish to either view Line chart or a Frequency diagram of the National Daily Deaths? [LC/FD]"))
        if q1_2 == "LC":
            plt.title("National Daily Deaths in result of Covid")
            plt.plot(nd.Date, nd.National_Daily_Deaths, "b.-")
            plt.xticks(nd.Date[::75])
            plt.xlabel("Day")
            plt.ylabel("Casualties")
            plt.show()
        elif q1_2 == "FD":
            bins = [0,10,20,30,40,50,60,70,80,90,100,110,120]
            plt.title("Frequency of National Daily Deaths in result of Covid")
            plt.hist(nd.National_Daily_Deaths, bins=bins)
            plt.xticks(bins)    
            plt.yticks()
            plt.ylabel("Casualties")
            plt.show()
            #Basically shows the frequency of how many people can die a day, for an exampel the chance of
            #only 1 person dying every day is very high compared to 120 people dying which is very low
    elif q1 == "NTDAG":
        q1_3 = str(input("Do you wish to either view Pie chart or a Bar chart of the National Daily Deaths by Age Group? [PC/BC]"))
        if q1_3 == "PC":
            labels = ["0-9", "10-19", "20-29", "30-39", "40-49", "50-59", "60-69", "70-79", "80-89", "90+"]
            plt.title("Total percentage of casualites withing age groups")
            plt.pie(nt.Total_Deaths, labels = labels, autopct="%.2f %%")
            plt.show()
        if q1_3 == "BC":
            print("g")
            #Loads the bar chart of NTDAG
    elif q1 == "NEITHER":
        run = False
