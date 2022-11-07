from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorecard import Scorecard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title(titlestring="Welcome to Pong")
screen.tracer(0)

paddle_r = Paddle((350,0))
paddle_l = Paddle((-350,0))
ball = Ball()
scorecard = Scorecard()


screen.listen()
screen.onkey(paddle_r.go_up, "Up")
screen.onkey(paddle_r.go_down, "Down")
screen.onkey(paddle_l.go_up, "w")
screen.onkey(paddle_l.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    
    #Detect R paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scorecard.increase_score_player_2()

    #Detect L paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scorecard.increase_score_player_1()

screen.exitonclick()