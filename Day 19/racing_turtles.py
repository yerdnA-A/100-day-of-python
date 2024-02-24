from turtle import Turtle, Screen
import random

mickey = Turtle(shape='turtle')
don = Turtle(shape='turtle')
rapha = Turtle(shape='turtle')
leo = Turtle(shape='turtle')

mickey.color('orange')
don.color('purple')
rapha.color('red')
leo.color('blue')

mickey.name = 'Mickey'
don.name = 'Don'
rapha.name = 'Rapha'
leo.name = 'Leo'

all_t = [mickey, don, rapha, leo]

mickey.pu()
don.pu()
rapha.pu()
leo.pu()

mickey.goto(-250,75)
don.goto(-250, 25)
rapha.goto(-250, -25)
leo.goto(-250, -75)


while True:
    for t in all_t:
        move = random.randint(1,30)
        t.forward(move)
        if t.xcor() >= 250:
            win_t = t
            break
    else:
        continue
    break

print(f"{win_t.name} win")


screen = Screen()
screen.exitonclick()