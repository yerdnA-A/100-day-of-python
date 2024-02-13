import turtle as t
import random

mickey = t.Turtle()

mickey.speed(0)
mickey.hideturtle()
t.colormode(255)
mickey.penup()


colours = [(102, 34, 204),    (63, 191, 215),    (145, 102, 197),    (13, 227, 175),    (68, 10, 66),    (240, 60, 209),    (16, 135, 209),    (34, 133, 84),    (81, 196, 225),    (139, 153, 124),    (203, 69, 47),  (206, 149, 95),    (230, 26, 160),    (92, 158, 120),    (101, 152, 215),    (83, 52, 67),    (25, 76, 101), (9, 187, 163),    (59, 53, 132),    (181, 14, 75)]

def circle_draw(x, y, raio, cor):
    mickey.goto(x,y)
    mickey.pd()
    mickey.begin_fill()
    mickey.color(cor)
    mickey.circle(raio)
    mickey.end_fill()
    mickey.pu()

screen_size = 600
num_points_side = 10
space_points = screen_size / num_points_side

for i in range(num_points_side):
    for j in range(num_points_side):
        x = (-screen_size / 2) + (i * space_points) + (space_points / 2)
        y = (-screen_size / 2) + (j * space_points) + (space_points / 2)
        cor = random.choice(colours)
        circle_draw(x, y, 20, cor)

screen = t.Screen()
screen.exitonclick()
