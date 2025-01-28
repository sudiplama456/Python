import numpy as np
import matplotlib.pyplot as plt

x_vals = np.linspace(-5, 5, 100)
y1 = 2 * x_vals + 1
y2 = 2 * x_vals + 2
y3 = 2 * x_vals + 3

plt.figure(figsize=(8, 6))
plt.plot(x_vals, y1, 'k-', label='y=2x+1')
plt.plot(x_vals, y2, 'k--', label='y=2x+2')
plt.plot(x_vals, y3, 'k-.', label='y=2x+3')

plt.title("Graphs of y=2x+1, y=2x+2, y=2x+3", fontsize=14)
plt.xlabel("x-axis", fontsize=12)
plt.ylabel("y-axis", fontsize=12)
plt.grid(True, linestyle=':', color='gray', alpha=0.7)
plt.legend(fontsize=10)
plt.show()
