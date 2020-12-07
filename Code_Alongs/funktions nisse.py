
a = int(input("Vad är talet a?"))
b = int(input("Vad är talet b?"))

def medelvärde(a,b):
    medel = (a+b)/2 #Medel är en lokal variable för bara medelvärde funktionen
    return medel


vikt_medel = medelvärde(a,b)

print(f"Min medel vikt är {vikt_medel}")