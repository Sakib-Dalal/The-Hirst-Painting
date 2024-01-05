import colorgram
""" for more info about colorgram visit link:- https://pypi.org/project/colorgram.py/"""

import turtle as t
import random

color = colorgram.extract("image.jpg", 30)

my_colors_list = []

for i in range(len(color)):
    my_tuple_rgb = (color[i].rgb.r, color[i].rgb.g, color[i].rgb.b)
    my_colors_list.append(my_tuple_rgb)

print(my_colors_list)

# turtle work here
t.colormode(255)
my_turtle = t.Turtle()
my_screen = t.Screen()


def draw(dots):
    x_pos = -335
    y_pos = -300
    for i in range(dots):
        for j in range(dots):
            my_turtle.penup()
            my_turtle.setposition(x_pos, y_pos)
            print(my_turtle.position())
            my_turtle.pendown()
            my_turtle.dot(20, random.choice(my_colors_list))
            my_turtle.penup()
            my_turtle.forward(50)
            my_turtle.pendown()
            x_pos += 50
        x_pos = -335
        y_pos += 50


""" change number of dots as you required"""
draw(dots=15)
my_screen.exitonclick()
