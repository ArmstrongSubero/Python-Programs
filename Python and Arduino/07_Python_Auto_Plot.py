import numpy as np
import matplotlib.pyplot as plt

#x = np.arange(-3, 4, 0.1)  # create x array
x = np.linspace(-3, 3, 100)  # -3 to 3 with 100 points
y = x**2   # create y array
z = (x - 2) ** 2

plt.plot(x, y, 'b-', label = 'y = x^2')           # blue line
plt.plot(x, z, 'r-', label = 'y = (x - 2) ** 2')  # red line
plt.legend()
plt.title('My quadratic')
plt.xlabel('My X values')
plt.ylabel('My Y values')
plt.show()
