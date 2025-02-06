import matplotlib.pyplot as plt
import numpy as np

xPoints = np.array([0, 6])

yPoints = np.array([0, 250])

plt.plot(xPoints, yPoints, marker = 'o')

# plt.plot(xPoints, yPoints,'o') # Sample Plot with points only

# plt.plot(xPoints, yPoints, linestyle = 'dotted', marker = 'o') # Sample Plot with points and dotted line

plt.title("Sample Plot")

plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.show()