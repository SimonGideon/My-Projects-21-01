# Python Program to draw rainbow Benzene
import turtle
from turtle import *
# Importing turtle library
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
t.speed(10)
turtle.bgcolor('black')
for x in range(360):
    t.shape("turtle")
    t.pencolor(colors[x % 6])
    t.width(x/100 +2)
    t.forward(x)
    # t.left(59)
    t.right(59)
t.hideturtle()
turtle.done()
