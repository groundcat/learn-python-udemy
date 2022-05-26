from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):

        # Call the parent class constructor
        super().__init__()

        # Set the ball's position
        self.penup()
        self.x_move = 10
        self.y_move = 10

        # Set the ball's size
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5)

    def move(self):
        """
        Initialize the ball's movement
        """
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Bounce the ball
    def bounce_y(self):
        """
        Bounce the ball off the y direction
        """
        self.y_move *= -1

    def bounce_x(self):
        """
        Bounce the ball off the x direction
        """
        self.x_move *= -1

    # Reset the ball's position
    def reset(self):
        """
        Reset the ball's position
        """
        self.goto(0, 0)
        self.bounce_x()




