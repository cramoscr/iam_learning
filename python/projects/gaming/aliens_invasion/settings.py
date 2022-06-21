# settings.py
# -----------
# Updated: cramos 12/jun/2022
# This is part of the AliensInvasion project
# Based on PythonCrashCourse book (page 229)

class Settings:
	""" A class to store all settings of the Aliens Invasion """
	def __init__(self):
		""" Initialize the game's settings """
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship settings
		self.ship_speed = 1.5
		self.ship_limit = 3

		# Bullet settings
		self.bullet_speed = 1.5
		self.bullet_width = 300      # n pixels
		self.bullet_height = 15      # n pixels
		self.bullet_color = (60, 60, 60)
		self.bullets_allowed = 3

		# Alien settings
		self.alien_speed = 0.75
		self.fleet_drop_speed = 10
		# fleet_direction pf 1 represents right; -1 represents left
		self.fleet_direction = 1
