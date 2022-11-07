import colorgram
from turtle import Turtle, Screen

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
print(colors)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colors.append(new_color)

tur = Turtle()

for i in range (0,10):
    tur.stamp

print(rgb_colors)