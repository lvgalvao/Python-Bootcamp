from turtle import Turtle
import time

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]


body = []
snack_size = 3
game_is_starting = True

class Snake:

    def __init__(self) -> None:
        self.body = []
        self.create_snake()

# task 02 - create a snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_body = Turtle('square')
            new_body.color('white')
            new_body.penup()
            new_body.goto(position)
            self.body.append(new_body)

# task 03 - move the snake
    def move(self):
        for seg_nun in range (len(self.body) -1, 0, -1):
            new_x = self.body[seg_nun - 1].xcor()
            new_y = self.body[seg_nun - 1].ycor()
            self.body[seg_nun].goto(new_x, new_y)
        self.body[0].forward(20)
