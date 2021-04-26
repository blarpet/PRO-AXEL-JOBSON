import random as rnd
import numpy as np

numbers = []

for i in range(10):
  numbers.append(rnd.randint(1,100))
arrayNumbers = np.array(numbers)

print(arrayNumbers)
print("")
print(arrayNumbers*2)