from turtle import Turtle
FONT = ("arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280,280)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", font=(FONT))

    def increase_score(self):
        self.level += 1
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over.\nFinal level: {self.level}",align= "center",font=FONT)