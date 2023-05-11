from turtle import Turtle
import random

COLOURS = ["blue", "yellow", "red", "orange", "green"]
STARTING_MOVE_SPEED = 5


class Car():
    def __init__(self):
        self.level_speed = 10
        self.all_cars = []


    def create_car(self):
        random_chance = random.randint(1,4)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.color(COLOURS[random.randint(0,4)])
            new_car.setheading(180)
            new_car.location = random.randint(-270, 290)
            new_car.goto(320, new_car.location)
            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.forward(self.level_speed)

    def level_up(self):
        self.level_speed += 10