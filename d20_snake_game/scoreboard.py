from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 12, 'normal')
Y_LOC = 280

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, Y_LOC)
        self.color("white")
        self.hideturtle()
        self.add_score()

    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)