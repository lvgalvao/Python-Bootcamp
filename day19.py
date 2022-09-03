from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
# task 01 - move forwards
screen.onkey(move_forwards, key='w')

# task 02 - move backwards

screen.onkey(move_backwards, 's')

# task 03 - counter-clockwise

screen.onkey(counter_clockwise, 'a')    

# task 04 - clockwise

screen.onkey(clockwise, 'd')    
# task 05 - clear drawing

screen.onkey(clear, 'c')   

screen.exitonclick()
