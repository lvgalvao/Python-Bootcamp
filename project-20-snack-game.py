# task 01 - setup the screen
# task 02 - create a snake body
# task 03 - move the snake
# task 04 - create snake food
# task 05 - detect collision with food
# task 06 - create a scoreboard
# task 07 - detect collision with wall
# task 08 - detect collision with tail

from turtle import Turtle, Screen

# task 01 - setup the screen

screen = Screen()
screen.screensize(600,600)
screen.bgcolor("black")
screen.title(titlestring="Welcome to the Snack Game")

# task 02 - create a snake body

snack_body = []
snack_size = 3
position_init = [0,-20,-40]

for n in range(0, snack_size):
    new_square = Turtle()
    new_square.shape('square')
    new_square.color('white')
    new_square.penup()
    new_square.goto(position_init[n],0)
    snack_body.append(new_square)









screen.exitonclick()
