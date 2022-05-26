from turtle import Turtle, Screen

timmy = Turtle()  # create an instance
print(timmy)
timmy.shape("turtle")  # use the shape method to change the shape to a turtle
timmy.color("coral")  # change color
timmy.forward(100)  # move forward by 100 paces

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()  # allow the screen continue to run until you click on the screen

