# snake_food_class.py
# ----------------
# Updated: cramos 26/ago/2022

import random
from turtle import Screen, Turtle
from snake_class import Snake

# Food class inherith from Turtle !!!
class Food(Turtle):

	def __init__(self):
		super().__init__()
		self.shape("circle")
		self.penup()
		self.shapesize(stretch_len=0.65, stretch_wid=0.65)
		self.color("pink")
		self.speed("fastest")
		self.refresh()

	def refresh(self):
		random_x = random.randint(-280, 280)
		random_y = random.randint(-280, 280)
		self.goto(random_x, random_y)


