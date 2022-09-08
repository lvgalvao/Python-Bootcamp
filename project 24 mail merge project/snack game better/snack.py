from turtle import Turtle
import time

STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

body = []

class Snake:

    def __init__(self) -> None:
        self.body = []
        self.create_snake()
        self.head = self.body[0]

# task 02 - create a snake body
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

# task 08 - add segment

    def add_segment(self, position):
        new_body = Turtle('square')
        new_body.color('white')
        new_body.penup()
        new_body.goto(position)
        self.body.append(new_body)

    def extend(self):
        self.add_segment(self.body[-1].position())


# task 03 - move the snake
    def move(self):
        for seg_nun in range (len(self.body) -1, 0, -1):
            new_x = self.body[seg_nun - 1].xcor()
            new_y = self.body[seg_nun - 1].ycor()
            self.body[seg_nun].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for body in self.body:
            body.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]
