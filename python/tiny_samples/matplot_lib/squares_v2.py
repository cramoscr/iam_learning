# matplot_squares_v2.py
# ------------------
# Updated: cramos 25/jun/2022
# Playing with MatPlotLib
# Based on PythonCrashCourse book (page 306)

import matplotlib.pyplot as plt 

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()

ax.plot(input_values, squares, linewidth=2)

# Set chart tittle and label
ax.set_title ("This is the main Title", fontsize=24)
ax.set_xlabel ("x axis label", fontsize=14)
ax.set_ylabel ("y axis label", fontsize=14)

# Set the size of tick labels
ax.tick_params(axis='both', labelsize=14)

# Open a MatPlotLib viewer with the generated plot
plt.show()
