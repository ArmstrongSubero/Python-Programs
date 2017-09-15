import numpy as np
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, 'bo')
plt.plot(x, y, 'r-')
plt.title("My line graph")
plt.xlabel("My X axis")
plt.ylabel("Y = 2 * X")
plt.grid(True)
plt.show()
