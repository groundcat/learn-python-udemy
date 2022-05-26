from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("red")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    for _ in range(num_sides):
        tim.color(random.choice(colours))
        angle = 360/num_sides
        tim.lt(angle)

        # draw dashed lines
        for _ in range(10):
            tim.fd(8)
            tim.penup()
            tim.fd(8)
            tim.pendown()


for n in range(3, 8):
    draw_shape(n)


screen = Screen()
screen.exitonclick()