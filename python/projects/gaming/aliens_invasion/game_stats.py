# game_stats.py
# -------------
# Updated: cramos 20/jun/2022
# This is part of the AliensInvasion project
# Based on PythonCrashCourse book (page 273)

import pygame

class GameStats:
	""" Track statistics for Alien Invasion """
	def __init__(self, ai_game):
		""" Initialize statistics """
		self.settings = ai_game.settings
		self.reset_stats()

		# Start Alien Invasion in an inactive state
		self.game_active = False

	def reset_stats(self):
		""" Initialize statistics that can change during the game """
		self.ships_left = self.settings.ship_limit
