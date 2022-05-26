import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
turtle.colormode(255)

tim.shape("turtle")
tim.color("red")
tim.pensize(10)
tim.speed("fastest")


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color  # return as a tuple


for _ in range(200):
    tim.color(rand_color())
    angle = 90 * random.choice([1, -1])  # random direction
    tim.lt(angle)
    tim.fd(10 * random.choice([1, 2, 3, 4]))  # random distance


screen = Screen()
screen.exitonclick()
