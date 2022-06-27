# chart_without_lines.py
# -------------------
# Updated: cramos 25/jun/2022
# Playing with MatPlotLib
# Based on w3schools.com examples

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 6, 8])
ypoints = np.array([3, 7, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()
