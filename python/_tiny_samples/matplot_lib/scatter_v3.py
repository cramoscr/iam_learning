# scatter_v3.py
# ----------
# Updated: cramos 25/jun/2022
# Playing with MatPlotLib
# Based on PythonCrashCourse book (page 310)
# Scattering allows to empathize some particular points of data

import matplotlib.pyplot as plt 

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# Adding UI effects
plt.style.use('seaborn-v0_8')    # Use: plt.style.available to see options
fig, ax = plt.subplots()

# Generating the scatter point.  s=visual size of the dot, c=line color
ax.scatter(x_values, y_values, c='red', s=10)

# Set chart tittle and label
ax.set_title ("This is the main Title", fontsize=24)
ax.set_xlabel ("x axis label", fontsize=14)
ax.set_ylabel ("y axis label", fontsize=14)

# Set the size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Set the range for each axis.
ax.axis([0, 1100, 0, 1100000])

# Open a MatPlotLib viewer with the generated plot
plt.show()
