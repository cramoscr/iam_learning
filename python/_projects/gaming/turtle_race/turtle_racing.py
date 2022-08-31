# turtle_racing.py
# -------------
# Updated: cramos 25/ago/2022
# Based on TheLondonApp Brewery 100Days_Of_Python_Code
# Turtle lib tips:
#    Initial position is x=0,y=0 on the center of the window square
#    Negative values of x means left
#    Negative values of y means down

import random

from turtle import Turtle, Screen

colors = ['yellow', 'cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'brown', 'orange']
all_turtles = []
is_race_on = False

screen = Screen()
screen.setup(width=600, height=500)

# Step 2 - Asking the user
user_bet = screen.textinput(title="Make your Bet... ", prompt="Which color will win ? :")
print(f'User_bet: {user_bet}')


# Step 3 - Dealing with turtles initial position

def new_turtle(p_color, p_x, p_y):
	my_turtle = Turtle(shape="turtle")
	my_turtle.color(p_color)
	my_turtle.penup()
	my_turtle.goto(x=p_x, y=p_y)
	all_turtles.append(my_turtle)

x_val = -260
y_val = -170

for i in range(0, 6):
	new_turtle(colors[i], x_val, y_val)
	y_val += 40

# Main section

if user_bet:
	is_race_on = True

while is_race_on:
	for turtle in all_turtles:
		if turtle.xcor() > 250:
			is_race_on = False
			winner_color = turtle.pencolor()
			if winner_color == user_bet:
				print(f"You've won! The {winner_color} turtle is the winner")
			else:
				print(f"You've lost! The {winner_color} turtle is the winner")

		rand_distance = random.randint(0, 10)
		turtle.forward(rand_distance)

screen.exitonclick()
