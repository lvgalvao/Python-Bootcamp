### goal is create a race using the turtle module

## task 01 - import the modules
## task 02 - create 6 instances of turtles spaced in 30y
## task 03 - the user need to choose a color
## task 04 - all turtles need to walk a randon distance
## task 05 - the first turtle to cros the line 
## task 06 - check if was the turtle choosed by the user
## task 07 - if was, the user won and if was not the user lost

## task 01 - import the modules
from turtle import Turtle, Screen
import random

## task 02 - create 6 instances of turtles spaced in 30y

screen = Screen()
screen.title("Welcome to the turtle race!")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
y_position = [-70, -40, -10, 20, 50, 80, 110]
turtles = []
is_race_on = False

## task 03 - the user need to choose a color
user_bet = screen.textinput(title="Bet",prompt= "which turtle will win the race? Enter a color: ")

for n in range(len(colors)):
    turtle = Turtle()
    turtle.shape('turtle')
    turtle.penup()
    turtle.color(colors[n])
    turtle.goto(-300,y_position[n])
    turtles.append(turtle)


if user_bet:
    is_race_on = True

## task 04 - all turtles need to walk a randon distance

while is_race_on:
    
    for n in turtles:
        if n.xcor() > 230:
            is_race_on = False
            if user_bet == n.color():
                print(f"you won! the {n.color()} is the winner")
            else:
                print(f"you lose! the {n.color()} is the winner")
        n.forward(random.randint(0,10))




screen.exitonclick()





































# import random
# from turtle import Turtle, Screen

# is_race_on = False
# screen = Screen()
# screen.setup(width=500, height=400)
# user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
# print(user_bet)

# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# y_position = [-70, -40, -10, 20, 50, 80, 110]
# all_turtle = []


# for turtle_index in range (0, 6):
#     new_turtle = Turtle(shape='turtle')
#     new_turtle.penup()
#     new_turtle.color(colors[turtle_index])
#     new_turtle.goto(x=-230,y=y_position[turtle_index])
#     all_turtle.append(new_turtle)

# if user_bet:
#     is_race_on = True

# while is_race_on:

#     for turtle in all_turtle:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f"You've won! the {winning_color} turtle is the winner!")
#             else:
#                 print(f"You've lost! the {winning_color} turtle is the winner!")
#         rand_distance = random.randint(0, 10)
#         turtle.forward(rand_distance)

# screen.exitonclick()