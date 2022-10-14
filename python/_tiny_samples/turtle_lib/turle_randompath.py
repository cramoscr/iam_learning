#turtle_randompath.py
# -----------------
# Updated: cramos 20/ago/2022
# Small Turtle project.

# Resources
#    https://docs.python.org/3/library/turtle.html
#    https://cs111.wellesley.edu/labs/lab02/colors

# Turtle library is part of the standard python lib
import turtle
from turtle import Screen, Turtle
import random

turtle.colormode(255)

# Using module ALIAS
# import Turtle as t
# my_turtle = t.Turtle()

# Press the green button in the gutter to run the script.

colors = ["medium blue", "sea green", "orange red", "magenta", "gold", "blue"]
directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

def random_walk():

    my_turtle.pensize(15)
    my_turtle.speed("fastest")

    for _ in range(100):
        my_turtle.color(random_color())
        my_turtle.forward(30)
        my_turtle.setheading(random.choice(directions))

def draw_shape (qty_sides, side_length):
    angle = 360 / qty_sides
    for _ in range(0, qty_sides):
        my_turtle.forward(side_length)  # Move the turtle 100 pixels forward
        my_turtle.left(angle)  # Move the turtle 100 pixels forward

if __name__ == '__main__':

    my_turtle = Turtle()
    my_turtle.shape("turtle")
    my_turtle.color("navy")    # More colors: https://cs111.wellesley.edu/labs/lab02/colors

    # Example 1 - Draw a square on the screen
    #for _ in range(1, 5):
    #    my_turtle.forward(100)  # Move the turtle 100 pixels forward
    #    my_turtle.left(90)   # Turn the turtle 90 grades to the left

    # Example 2 - Draw a dotted line
    #for _ in range(1, 10):
    #    my_turtle.pendown()  # Move the turtle 100 pixels forward
    #    my_turtle.forward(10)  # Move the turtle 100 pixels forward
    #    my_turtle.penup()  # Move the turtle 100 pixels forward
    #    my_turtle.forward(10)  # Move the turtle 100 pixels forward

    # Example 3 - Draw different kind of shapes
    #for sides in range(3, 11):
    #    my_turtle.color(random.choice(colors))
    #    draw_shape(sides, 100)

    # Example 4 - Random walk
    random_walk()

    # Start a new screen window
    my_screen = Screen()
    my_screen.exitonclick()

