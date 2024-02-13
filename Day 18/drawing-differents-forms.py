import turtle as t
import tkinter as TK

don = t.Turtle()

def triangle():
    don.color('red')
    for i in range(3):
        don.forward(100)
        don.right(120)

def square():
    don.color('purple')
    for i in range(4):
        don.forward(100)
        don.right(90)

def pentagon():
    don.color("blue")
    for i in range(5):
        don.forward(100)
        don.right(72)

def hexagon():
    don.color("orange")
    for i in range(6):
        don.forward(100)
        don.right(60)

def heptagon():
    don.color("green")
    for i in range(7):
        don.forward(100)
        don.right(51.428571429)

def octagon():
    don.color("yellow")
    for i in range(8):
        don.forward(100)
        don.right(45)

def nonagon():
    don.color("red")
    for i in range(9):
        don.forward(100)
        don.right(40)
    
def decagon():
    don.color("black")
    for i in range(10):
        don.forward(100)
        don.right(36)

triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

screen = t.Screen()
screen.exitonclick()