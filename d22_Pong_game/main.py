from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


# Create a screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)  # Turns off the screen updates

# Create paddles with the paddle class
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Create a ball with the ball class
ball = Ball((0, 0))

# Create a scoreboard with the scoreboard class
scoreboard = ScoreBoard()

# Control the paddles with the arrow keys and w and s keys
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Update the screen while the game is running
game_is_on = True
while game_is_on:
    screen.update()
    ball.move()  # Move the ball to the top right corner
    time.sleep(0.1)  # Slow down the game

    # Check if the ball hits the walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        # Bounce the ball
        ball.bounce_y()

    # Check if the ball hits the paddles
    if ball.distance(r_paddle) < 100 and ball.xcor() > 280 or ball.distance(l_paddle) < 100 and ball.xcor() < -280:
        ball.bounce_x()

    # Check if the right paddle misses the ball
    if ball.xcor() > 390:
        # Reset the ball
        ball.reset()
        # Increase the score of the left player
        scoreboard.record_score("left")

    # Check if the left paddle misses the ball
    if ball.xcor() < -390:
        # Reset the ball
        ball.reset()
        # Increase the score of the right player
        scoreboard.record_score("right")

# Exit on click
screen.exitonclick()