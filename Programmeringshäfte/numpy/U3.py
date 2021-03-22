import numpy as np
import matplotlib.pyplot as plt 


x = np.linspace(0,10)

def f(x):
    y = 3*x+1
    return y

plt.plot(x,f(x))
plt.title("y = 3x + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.show()