# task 06 - create a scoreboard
# task 07 - detect collision with wall
# task 08 - detect collision with tail

from turtle import Screen
from snack import Snake
from food import Food
import time

# task 01 - setup the screen

screen = Screen()
screen.screensize(600,600)
screen.bgcolor("black")
screen.title(titlestring="Welcome to the Snack Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# task 05 - detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()












screen.exitonclick()