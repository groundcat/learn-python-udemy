import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create player
player = Player()
screen.listen()
screen.onkey(player.go_up, "Up")

# Create cars
car_list = []
for i in range(200):
    new_car = CarManager()
    car_list.append(new_car)

# Create scoreboard
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_list:
        car.move()
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
        if player.ycor() > FINISH_LINE_Y:
            scoreboard.increase_level()
            player.goto(0, -200)


