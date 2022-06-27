# scatter.py
# -------
# Updated: cramos 25/jun/2022
# Playing with MatPlotLib
# Based on PythonCrashCourse book (page 310)
# Scattering allows to empathize some particular points of data

import matplotlib.pyplot as plt 

#input_values = [1, 2, 3, 4, 5]
#squares = [1, 4, 9, 16, 25]

# Adding UI effects
plt.style.use('seaborn-dark')    # Use: plt.style.available to see options

fig, ax = plt.subplots()

# Generating the scatter point.  s=visual size of the dot
ax.scatter(2, 4, s=300)

# Set chart tittle and label
ax.set_title ("This is the main Title", fontsize=24)
ax.set_xlabel ("x axis label", fontsize=14)
ax.set_ylabel ("y axis label", fontsize=14)

# Set the size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Open a MatPlotLib viewer with the generated plot
plt.show()
