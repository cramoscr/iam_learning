# snake_scoreboard_class.py
# ----------------------
# Updated: cramos 26/ago/2022

# Based on TheLondonApp 100DaysOfPython

from turtle import Screen, Turtle

ALIGNMENT = "Center"
FONT = ("Arial", 24, "normal")

# Scoreboard class inherith from Turtle !!!
class Scoreboard(Turtle):

	def __init__(self):
		super().__init__()
		self.score = 0
		self.color("white")
		self.penup()
		self.goto(x=0, y=240)
		self.hideturtle()
		self.write (f"Score: {self.score}", align=ALIGNMENT, font=FONT)
		self.update_scoreboard()

	def update_scoreboard(self):
		self.write (f"Score: {self.score}", align=ALIGNMENT, font=FONT)

	def game_over(self):
		self.goto(0, 0)
	   #self.clear()
		self.write (f"GAME OVER", align=ALIGNMENT, font=FONT)

	def increase_score(self):
		self.score += 1
		self.clear()
		self.update_scoreboard()

