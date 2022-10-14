# rolling_dice_class.py
# ------------------
# Updated: cramos 26/jun/2022
# Playing with Plotly
# Based on PythonCrashCourse book (page 324)

from random import randint

class Dice:
	""" A class representing a single dice """

	def __init__(self, num_sides=6):
		""" Assume a six-sided dice """
		self.num_sides = num_sides

	def roll(self):
		""" Return a random value between 1 and num_sides """
		return randint(1, self.num_sides)

