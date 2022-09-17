from turtle import Turtle
import random
FOOD_COLOR = "red"
FOOD_SHAPE = "circle"

# task 04 - create snake food

class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        random_x = random.randint(-320,320)
        random_y = random.randint(-320,320)
        self.goto(random_x, random_y)