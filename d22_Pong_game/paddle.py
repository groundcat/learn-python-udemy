from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):

        # Call the parent class constructor
        super().__init__()

        # Create a paddle
        self.paddle = Turtle()
        self.paddle.penup()
        self.paddle.speed("fastest")
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.goto(position)

    def go_up(self):
        """
        Move the paddle up
        """
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(self.paddle.xcor(), new_y)

    def go_down(self):
        """
        Move the paddle down
        """
        new_y = self.paddle.ycor() - 20
        self.paddle.goto(self.paddle.xcor(), new_y)
