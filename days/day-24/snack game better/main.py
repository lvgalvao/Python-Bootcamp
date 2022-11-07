from turtle import Screen
from snack import Snake
from food import Food
from scorecard import Scorecard
import time

# task 01 - setup the screen

screen = Screen()
screen.screensize(600,600)
screen.bgcolor("black")
screen.title(titlestring="Welcome to the Snack Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorecard = Scorecard()

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
        snake.extend()
        scorecard.increase_score()

# task 07 - detect collision with wall

    if snake.head.xcor() > 350 or snake.head.xcor() < -350 or snake.head.ycor() > 350 or snake.head.ycor() < -350:
        game_is_on = True
        scorecard.reset()
        snake.reset()

# task 09 - detect collision with tail

    for segment in snake.body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = True
            scorecard.reset()
            snake.reset()












screen.exitonclick()