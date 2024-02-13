import turtle as t
import random

leo = t.Turtle()

raio = 100

leo.speed("fastest")

t.colormode(255)

def color_mode():
    r = (random.randint(0,255))
    g = (random.randint(0,255))
    b = (random.randint(0,255))
    tup = (r, g, b)
    leo.pencolor(tup)


for i in range(0,360,10):
    leo.circle(100)
    leo.right(10)
    color_mode()

screen = t.Screen()
screen.exitonclick()