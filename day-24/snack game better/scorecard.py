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
        with open("project 24 mail merge project/highscore.txr", mode="r") as file:
            self.highscore = int(file.read())
        self.color(SCORECARD_COLOR)
        self.penup()
        self.goto(SCORECARD_COORDINATE)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()        
        self.write(f"Scorecard = {self.score} and high score = {self.highscore}", align=ALIGHMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("project 24 mail merge project/highscore.txr", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
        # self.goto(0,0)


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGHMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()