from turtle import Turtle, Screen

tim = Turtle()
tim.setheading(90)

screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_clockwise():
    tim.circle(-120, extent=10)


def move_anticlockwise():
    tim.circle(120, extent=10)


def clear_drawings():
    tim.penup()
    tim.clear()
    tim.setposition(0, 0)
    tim.pendown()
    tim.setheading(90)


screen.listen()
# functions are used as inputs, passing func as an input of another func
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="a", fun=move_anticlockwise)
screen.onkey(key="c", fun=clear_drawings)

screen.exitonclick()
