from turtle import Turtle

STARTING_POSITION = (0, -200)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    
    def __init__(self, shape: str = "turtle") -> None:
        super().__init__(shape)
        self.color("black")
        self.penup()
        self.refresh()
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def refresh(self):
        self.goto(STARTING_POSITION)

        
