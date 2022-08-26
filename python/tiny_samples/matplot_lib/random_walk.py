# random_walk.py
# -----------
# Updated: cramos 25/jun/2022
# Playing with MatPlotLib
# Based on PythonCrashCourse book (page 316)
# Random walk is used in science (simulate real live [caotic] patterns)

import matplotlib.pyplot as plt
from random_walk_class import RandomWalk

# Make a random walk
rw = RandomWalk()
rw.fill_walk()

# Plot the points in the walk
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)

plt.show()
