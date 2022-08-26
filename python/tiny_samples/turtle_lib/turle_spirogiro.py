#turtle_spirogiro.py
# -----------------
# Updated: cramos 20/ago/2022
# Small Turtle project.

# Resources:
#    https://docs.python.org/3/library/turtle.html
#    https://cs111.wellesley.edu/labs/lab02/colors
# Notes:
#   Turtle library is part of the standard python lib

import turtle
from turtle import Screen, Turtle
import random

turtle.colormode(255)

colors = ["medium blue", "sea green", "orange red", "magenta", "gold", "blue"]
directions = [0, 90, 180, 270]

def random_color():
    """ Returns a tuple containing a RBG color """    
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def draw_spirograph(gap_size, circle_size):
    """ Draws a spirograph """
    for _ in range (int(360 / gap_size)):
        my_turtle.color(random_color())    # More colors: https://cs111.wellesley.edu/labs/lab02/colors
        my_turtle.circle(circle_size)
        my_turtle.setheading(my_turtle.heading() + gap_size)

# Main body
if __name__ == '__main__':

    my_turtle = Turtle()
    my_turtle.shape("turtle")

    my_turtle.pensize(2)
    my_turtle.speed("fastest")
    
    draw_spirograph(5, 100)
    draw_spirograph(7, 120)
    draw_spirograph(9, 140)

    # Start a new screen window
    my_screen = Screen()
    my_screen.exitonclick()

