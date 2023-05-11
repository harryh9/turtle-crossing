from turtle import Screen
from player import Player
from cars import Car
from scoreboard import Scoreboard
import time
import random

# Create player and scoreboard
player = Player()
scoreboard = Scoreboard()

# Set up screen
screen = Screen()
screen.screensize(600,600)
screen.setworldcoordinates(-300,-300,300,300)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move, "space")

# create car objects
cars = Car()

# set up gameplay
t = 0.1
create_cars = True
game_is_on = True
while game_is_on:
    time.sleep(t)
    screen.update()
    cars.create_car()
    cars.move()
    for i in cars.all_cars:
        if i.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() >= 300:
        cars.level_up()
        player.start_pos()
        scoreboard.increase_score()
        t * 0.75


screen.exitonclick()