from turtle import Turtle
import car_manager

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(-250,200)

    def increase_scorecard(self):
        self.write(f"Level : {self.level}", align="left",font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.increase_scorecard()


    
