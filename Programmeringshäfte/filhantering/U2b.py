suckiList = []

with open('Provresultat.txt') as sucki:
    for rad in sucki:
        suckiList.append(rad.strip())
suckiList.sort()

with open('Provresultat.txt', 'a') as wacki:
    wacki.write('\n\nSorterade elever:')
    for rad in suckiList:
        wacki.write('\n' + rad)

for elever in suckiList:
    print(elever)