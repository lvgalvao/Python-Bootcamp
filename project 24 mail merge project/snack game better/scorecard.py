# task 06 - create a scoreboard

from turtle import Turtle
ALIGHMENT = "center"
FONT = ('Arial', 24, 'normal')
SCORECARD_COLOR = "white"
SCORECARD_COORDINATE = (0, 300)

class Scorecard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.color(SCORECARD_COLOR)
        self.penup()
        self.goto(SCORECARD_COORDINATE)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Scorecard = {self.score}", align=ALIGHMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGHMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()