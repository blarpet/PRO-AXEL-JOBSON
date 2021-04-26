import random
x = 0
results = {'dice1' : 0, 'dice2' : 0, 'dice3' : 0, 'dice4' : 0, 'dice5' : 0, 'dice6' : 0}

while x < 100001:
    y = random.randint(1,6)
    if y == 1:
        results['dice1'] += 1
    elif y == 2:
        results['dice2'] += 1
    elif y == 3:
        results['dice3'] += 1
    elif y == 4:
        results['dice4'] += 1
    elif y == 5:
        results['dice5'] += 1
    elif y == 6:
        results['dice6'] += 1
    x += 1
print(results)