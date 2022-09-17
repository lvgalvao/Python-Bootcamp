# task 08 - keep score

from turtle import Turtle

ALIGHMENT = "center"
FONT = ('Arial', 34, 'normal')
SCORECARD_COLOR = "white"
SCORECARD_COORDINATE = (0, 200)

class Scorecard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score_paddle_r = 0
        self.score_paddle_l = 0
        self.color(SCORECARD_COLOR)
        self.penup()
        self.goto(SCORECARD_COORDINATE)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score_paddle_r} vs {self.score_paddle_l}", align=ALIGHMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGHMENT, font=FONT)

    def increase_score_player_1(self):
        self.score_paddle_r += 1
        self.clear()
        self.update_scoreboard()

    def increase_score_player_2(self):
        self.score_paddle_l += 1
        self.clear()
        self.update_scoreboard()
