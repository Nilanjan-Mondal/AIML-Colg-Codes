import matplotlib.pyplot as plt
import numpy as np

xPoints = np.array([0, 6])

yPoints = np.array([0, 250])

plt.plot(xPoints, yPoints, marker = 'o')

plt.title("Sample Plot")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()