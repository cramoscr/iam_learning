# matplot_squares.py
# ---------
# Updated: cramos 25/jun/2022
# Playing with MatPlotLib
# Based on PythonCrashCourse book (page 306)

import matplotlib.pyplot as plt 

squares = [1, 4, 9, 16, 25]
squares = [1, 3.5, -1, 2, 5, 5.5, 5, 5, 5.3, 6, 6, 7, 10, 11, ]

fig, ax = plt.subplots()

ax.plot(squares)

# Open a MatPlotLib viewer with the generated plot
plt.show()
