import colorgram
import turtle
from turtle import Turtle, Screen
import random

# Extract colors from the jpg image
colors = colorgram.extract('2012_0112_Hirst_lead.jpg', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    if r < 240 and g < 240 and b < 240:  # exclude white shades
        new_color = (r, g, b)
        rgb_colors.append(new_color)
print(rgb_colors)

# Run the turtle
tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.speed("fastest")
tim.penup()
tim.hideturtle()


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color  # return as a tuple


def paint_dots(pace, num_rows):
    x = -300
    for _ in range(num_rows):
        x += pace
        tim.setposition(x, 300)
        for _ in range(num_rows):
            tim.setheading(270)
            tim.forward(pace)
            tim.dot(num_rows, rand_color())


paint_dots(40, 15)

screen = Screen()
screen.exitonclick()
