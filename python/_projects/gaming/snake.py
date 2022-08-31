# turtle_snake.py
# ------------
# Updated: cramos 26/ago/2022

from turtle import Screen
from snake_class import Snake
from snake_food_class import Food
from snake_scoreboard_class import Scoreboard

import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")

my_screen.tracer(0)

my_snake = Snake()
my_food = Food()
my_scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")

game_is_on = True
while game_is_on:
	my_screen.update()
	time.sleep(0.1)    # Introduces a pause (delay)	

	my_snake.move()

	# Detect Snake colission with the food
	if (my_snake.head.distance(my_food) < 15):
		my_food.refresh()
		my_scoreboard.increase_score()
		my_snake.extend()

	# Detect Snake colission with the wall
	if (my_snake.head.xcor() > 290) or (my_snake.head.xcor() < -290) or \
		(my_snake.head.ycor() > 290) or (my_snake.head.ycor() < -290):
		game_is_on = False
		my_scoreboard.game_over()

	# Detect Snake colission with the tail
	for segment in my_snake.segments:
		if segment == my_snake.head:
			pass
		elif my_snake.head.distance(segment) < 10:
			game_is_on = False
			my_scoreboard.game_over()

my_screen.exitonclick()