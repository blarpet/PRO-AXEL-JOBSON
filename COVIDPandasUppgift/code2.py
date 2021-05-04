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
            plt.plot(nd.Date, nd.National_Daily_Deaths)
            plt.xticks(nd.Date[::50])
            plt.xlabel("Day")
            plt.ylabel("Casualties")
            plt.show()