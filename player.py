from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.start_pos()


    def start_pos(self):
        self.setheading(90)
        self.goto(0,-290)

    def move(self):
        self.forward(10)

