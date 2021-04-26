import random as rnd

emptyList = []
antalFemmor = 0

for i in range(10):
    emptyList.append(rnd.randint(1,6))
        
for fem in emptyList:
    if fem == 5:
        antalFemmor += 1

print("De simulerade tärningskast: ", emptyList)

emptyList.sort()

with open('diceRoll.txt', 'w') as suckiwacki:
    suckiwacki.write(f"Sorterad kast: {emptyList}")

print("Kastet sorterat: ", emptyList)
print("Antal femmor: ", antalFemmor)