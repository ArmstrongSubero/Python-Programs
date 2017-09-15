import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
z = [2, 0, -2, -4, -6]

plt.plot(x, y, 'bo') # blue dots
plt.plot(x, y, 'r-', label = "y = 2x") # red line
plt.plot(x, z, 'g--', label = "y = -x + 4") # green dotted line
plt.plot(x, z, 'g^') # green triangles
plt.axis([0, 6, -8, 12]) #scale
plt.title("My line graph")
plt.xlabel("My X axis")
plt.ylabel("Y = 2 * X")
plt.grid(True)
plt.legend() # plot legend
plt.show()
