# random_walk_class.py
# -----------------
# Updated: cramos 25/jun/2022
# Playing with MatPlotLib
# Based on PythonCrashCourse book (page 316)
# Random walk is used in science (simulate real live [caotic] patterns)

from random import choice

class RandomWalk:
	""" A class to generate random walks """

	def __init__(self, num_point=500):
		""" Initialize attributes of a walk """
		self.num_points = num_point

		# All walks start at (0, 0)
		self.x_values = [0]
		self.y_values = [0]

	def get_step(self):
		""" Calculate the distance and direction of a single step """
		v_direction = choice([1, -1])
		v_distance = choice([0, 1, 2, 3, 4])
		v_step = v_direction * v_distance
		return v_step

	def fill_walk(self):
		""" Calculate all the points in the walk """

		# Keep taking steps until the walk reaches the desired lenght
		while len(self.x_values) < self.num_points:

			# Decide wich direction to go and how far to go
			x_step = self.get_step()
			y_step = self.get_step()

			# Reject moves that go nowhere
			if x_step == 0 and y_step == 0:
				continue

			# Calculate the new position (add the step value to last element)
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)
