import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 1000)
y = np.sqrt(x)*np.sin(x) + 4*np.sin(x)*np.cos(x*x)

plt.title("y = sqrt(x)*sin(x) + 4*sin(x)*cos(x^2)")
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
