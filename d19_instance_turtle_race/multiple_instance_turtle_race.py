from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
num_turtles = len(colors)
all_turtles = []

for turtle_id in range(0, num_turtles):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_id])
    new_turtle.penup()
    y_position = -100 + turtle_id * (200/(num_turtles-1))
    new_turtle.goto(x=-230, y=y_position)
    all_turtles.append(new_turtle)

# ask user to make a bet
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ")
print(user_bet)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if winner_color == user_bet:
                print(f"You've won! The winner is {winner_color} and you bet on {user_bet}")
            else:
                print(f"You've lost! The winner is {winner_color} but you bet on {user_bet}")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()