from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("red")
tim.pensize(10)
tim.speed("fastest")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]

for _ in range(200):
    tim.color(random.choice(colours))
    angle = 90 * random.choice([1, -1])  # random direction
    tim.lt(angle)
    tim.fd(10 * random.choice([1, 2, 3, 4]))  # random distance

screen = Screen()
screen.exitonclick()
