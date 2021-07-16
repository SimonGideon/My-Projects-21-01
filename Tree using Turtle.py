from turtle import *

tr = turtle.turtle()
tr.left(90)
tr.speed(150)


def tree(i):
    if i < 10:
        return
    else:
        tr.forward(i)
        tr.left(30)
        tree(3 * i / 4)
        tr.right(60)
        tree(3 * i / 4)
        tr.left(30)
        tr.backward(i)


tree(100)
turtle.done()
