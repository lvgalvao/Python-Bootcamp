import time
from turtle import Screen, Turtle
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
scoreboard.increase_scorecard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, 'Up')

is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    if player.ycor() > FINISH_LINE_Y - 10:
        print("level up")
        scoreboard.level_up()
        player.refresh()
        car_manager.level_up()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False

screen.exitonclick()