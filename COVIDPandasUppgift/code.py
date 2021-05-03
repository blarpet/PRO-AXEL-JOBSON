import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
run = True

nd = pd.read_csv("National_Daily_Deaths.csv")
nt = pd.read_csv("National_Total_Deaths_by_Age_Group.csv") 



while run = True:
    q1 = str(input("Do you wish to either view National Daily Deaths or the National Total Deaths by Age Group? [NDD/NTDAG/NEITHER]"))
    if q1 == "NDD":
        q1.2 = str(input("Do you wish to either view Line chart or a Frequency diagram of the National Daily Deaths? [LC/FD]"))
        if q1.2 == "LC":
            plt.title("National Daily Deaths in result of Covid")
            plt.plot(nd.date, nd.National_Daily_Deaths "b.-")
            plt.xticks(nd.date[::30])
            plt.xlabel("Day")
            plt.ylabel("Casualties")
            plt.show()
        elif q1.2 == "FD":
            #Loads the frequency diagram of the NDD
    if q1 == "NTDAG":
        q1.3 = str(input("Do you wish to either view Pie chart or a Bar chart of the National Daily Deaths? [PC/BC]"))
        if q1.3 == "PC":
            #Loads the pie chart of NTDAG
        if q1.3 == "BC":
            #Loads the bar chart of NTDAG
    elif q1 == "NEITHER":
        run = False
