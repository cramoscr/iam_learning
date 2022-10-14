# random_walk_v2.py
# --------------
# Updated: cramos 25/jun/2022
# Playing with MatPlotLib
#    https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.show.html
# Based on PythonCrashCourse book (page 316)
# Random walk is used in science (simulate real live [caotic] patterns)

import matplotlib.pyplot as plt
from random_walk_class import RandomWalk

# Make a random walk
rw = RandomWalk(50_000)
rw.fill_walk()

# Plot the points in the walk
plt.style.use('classic')

# figsize allows to set the output size
fig, ax = plt.subplots(figsize=(15,9), dpi=128)

point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
	cmap=plt.cm.Blues, edgecolors='none', s=1)

# Emphasize the first and last points
ax.scatter(0, 0, c='gray', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='blue', 
	edgecolors='none', s=100)

# Hide the axes leyends
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# This will produce a maximized window (requires a fine grained coordination with dpi parameter)
mng = plt.get_current_fig_manager()
#mng.full_screen_toggle()

# Starts a new window with the draw
plt.show()

