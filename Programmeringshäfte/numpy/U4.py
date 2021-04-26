import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2)

def f(x):
  y = x**2-1
  return y

plt.plot(x,f(x))
plt.title("y = x² - 1")
plt.xlabel("x")
plt.ylabel("y")
plt.figure()
plt.show()