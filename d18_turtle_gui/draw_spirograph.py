import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

tim.shape("turtle")
tim.speed("fastest")


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color  # return as a tuple


def draw_spirograph(num_circle):
    angle_delta = 360 / num_circle
    tim.setheading(0)
    for _ in range(num_circle):
        tim.color(rand_color())
        tim.right(angle_delta)
        tim.circle(100, extent=None, steps=360)  # random distance


draw_spirograph(100)  # paints 100 circles

screen = Screen()
screen.exitonclick()
