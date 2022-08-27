from turtle import *
import turtle as tur

tur.shape("turtle")
tur.color("red")

for i in range(0,200):
    tur.fd(10)
    tur.penup()
    tur.fd(10)
    tur.pendown()

tur.exitonclick()