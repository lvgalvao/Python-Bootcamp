# task 04 - create snake food
# task 05 - detect collision with food
# task 06 - create a scoreboard
# task 07 - detect collision with wall
# task 08 - detect collision with tail

from turtle import Turtle, Screen
from snack import Snack
import time

# task 01 - setup the screen

screen = Screen()
screen.screensize(600,600)
screen.bgcolor("black")
screen.title(titlestring="Welcome to the Snack Game")
screen.tracer(0)

snake = Snake()

game_is_starting = True



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)











screen.exitonclick()