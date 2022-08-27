from turtle import *
import turtle as tur
from random import choice

# tur.shape("turtle")
tur.color("red")

colours = ['green', 'pink', 'blue', 'yellow']
side = [0, 90, 180, 270]
tur.pensize(15)
tur.speed(500)


# lados = 12
# def draw_n_side(size):
#     angle = 360 / size
#     for i in range(0, size):
#         tur.fd(50)
#         tur.right(angle)

# def draw_n_sides(size):
#     for i in range(3,size):
#         angle = 360 / i
#         tur.color(choice(colours))
#         for j in range(0, i):
#             tur.fd(50)
#             tur.right(angle)
        

def randon_walk(steps):
    for i in range(0,steps):
        tur.setheading(choice(side))
        tur.fd(50)
        tur.color(choice(colours))

move = 50
randon_walk(move)

tur.exitonclick()
