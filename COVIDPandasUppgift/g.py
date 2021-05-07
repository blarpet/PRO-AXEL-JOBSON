import plotly.express as px
import numpy as np 
import pandas as pd 

antal = 10000000

tärningar = np.random.randint(1,7,antal) # simulerar antal tärningskast
utfall = np.bincount(tärningar)[1:] # beräknar frekvensen

# skapat dictionary
frekvens = dict(sida = np.arange(1,7), utfall = utfall)
#print(frekvens)

# skapa dataframe från dictionary
df = pd.DataFrame(frekvens)
print(df)