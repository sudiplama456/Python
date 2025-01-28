import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([-0.57, -2.57, -4.80, -7.36, -8.78, -10.52, -12.85, -14.69, -16.78])

plt.scatter(x, y, marker='+', color='black', label='(x, y) points')

plt.title('Scatter Plot of Points (x, y)')
plt.xlabel('x')  # Label for the x-axis
plt.ylabel('y')  # Label for the y-axis

plt.grid()
plt.legend()
plt.show()