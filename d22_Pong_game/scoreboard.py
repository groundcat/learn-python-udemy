from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):

        # Call the parent class constructor
        super().__init__()

        # Some attributes for the scoreboard
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)

        # Initialize the scores
        self.l_score = 0
        self.r_score = 0

        # Update the scoreboard
        self.update_score()

    def record_score(self, player):
        """
        Update the score of the specified player
        """
        if player == "left":
            self.l_score += 1
        else:
            self.r_score += 1

        # Update the scoreboard
        self.update_score()

    def update_score(self):
        # Update the scoreboard
        self.clear()
        self.write(f"{self.l_score} : {self.r_score}", align="center", font=("Courier", 24, "normal"))


