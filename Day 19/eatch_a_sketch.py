from turtle import Turtle, Screen

mickey = Turtle()

def move_fowards():
    mickey.forward(10)

def move_backwards():
    mickey.backward(10)

def clockwise():
    mickey.right(10)

def counter_clockwise():
    mickey.left(10)

def clear_drawing():
    mickey.clear()
    mickey.pu()
    mickey.home()
    mickey.pd()

screen = Screen()
screen.listen()
screen.onkey(key='w', fun=move_fowards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='c', fun=clear_drawing)

screen.exitonclick()