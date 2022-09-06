# task 01 - create the screen
# task 03 - create another paddle
# task 05 - detect collision with wall and bounce
# task 06 - detect collision with paddle
# task 07 - detect when paddle misses

from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")

paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)




screen.exitonclick()





