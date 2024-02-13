import turtle as t
import random

rapha = t.Turtle()

angles = [0, 90, 180, 270]
t.colormode(255)

rapha.speed('fastest')

def rotation():
    rapha.setheading(random.choice(angles))

def step():
    rapha.forward(30)
    r = (random.randint(0,255))
    g = (random.randint(0,255))
    b = (random.randint(0,255))
    tup = (r, g, b)
    rapha.pencolor(tup)


rapha.pendown()
rapha.pensize(15)

for i in range(100):
    step()
    rotation()


screen = t.Screen()
screen.exitonclick()