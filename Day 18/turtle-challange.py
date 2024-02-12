import tkinter as TK
import turtle as t

def square():
    for i in range(4):
        mickey.forward(100)
        mickey.left(90)

mickey = t.Turtle()
mickey.shape('turtle')
mickey.color('orange')

for i in range(30):
    mickey.pencolor('black')
    mickey.pendown()
    mickey.forward(5)
    mickey.penup()
    mickey.forward(5)


screen = t.Screen()
screen.exitonclick()