
amount = 0

myBalls = {
    "Matematik 3c": 100,
    "Idrott och Häsla": 100,
    "Engelska 6" : 100,
    "Programmering 1": 100,
    "Svenska 2" : 100,
    "Fysik 1a" : 100,
    "Webbutveckling 1" : 100,
    "Tillämpad programmering" : 100,
    "Dator- och nätverksteknik" : 100
    }
for line in myBalls:
    amount += myBalls[line]
print(amount)
