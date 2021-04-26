fList = []
eList = []
dList = []
cList = []
bList = []
aList = []

with open('Provresultat.txt', 'r') as sucki:

    for rad in sucki:

        points = int(rad[-3:-1])

        if points < 20:
            fList.append(rad.strip())
        elif points >= 20 and points <= 29:
            eList.append(rad.strip())
        elif points >= 30 and points <= 39:
            dList.append(rad.strip())
        elif points >= 40 and points <= 49:
            cList.append(rad.strip())
        elif points >= 50 and points <= 59:
            bList.append(rad.strip())
        elif points >= 60 and points <= 70:
            aList.append(rad.strip())

with open('Provresultat.txt', 'a') as wacki:
    
    wacki.write('\n\nF')
    for F in fList:
        wacki.write('\n' + F)
    
    wacki.write('\n\nE')
    for E in eList:
        wacki.write('\n' + E)
    
    wacki.write('\n\nD')
    for D in dList:
        wacki.write('\n' + D)
    
    wacki.write('\n\nC')
    for C in cList:
        wacki.write('\n' + C)
    
    wacki.write('\n\nA')
    for B in bList:
        wacki.write('\n' + B)

    wacki.write('\n\nA')
    for A in aList:
        wacki.write('\n' + A)

print("F")
for eleverF in fList:
    print(eleverF)

print("\nE")
for eleverE in eList:
    print(eleverE)

print("\nD")
for eleverD in dList:
    print(eleverD)

print("\nC")
for eleverC in cList:
    print(eleverC)

print("\nB")
for eleverB in bList:
    print(eleverB)

print("\nA")
for eleverA in aList:
    print(eleverA)