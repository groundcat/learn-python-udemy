from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        # Call the parent class constructor
        super().__init__()

        # Random color

        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=3)
        self.random_y = random.randint(-220, 250)
        self.random_x = random.randint(-6000, -300)
        self.penup()
        self.goto(self.random_x, self.random_y)
        self.setheading(0)
        self.color(random.choice(COLORS))

        # Move the car
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        """
        Initialize the ball's movement
        """
        self.forward(self.car_speed)