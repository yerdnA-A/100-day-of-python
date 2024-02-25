from turtle import Screen
from padle import Padle
from ball import Ball
from scoreboard import Score
import time 

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_padle = Padle((350, 0))
l_padle = Padle((-350, 0))
ball = Ball()
score = Score()

screen.onkey(key='Up', fun=r_padle.up)
screen.onkey(key='Down', fun=r_padle.down)

screen.onkey(key='w', fun=l_padle.up)
screen.onkey(key='s', fun=l_padle.down)

screen.listen()

game_is_on = True

while game_is_on:
    time.sleep(ball.spell)
    screen.update()
    ball.move()

    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()

    if ball.distance(r_padle) < 50 and ball.xcor() > 330 or ball.distance(l_padle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    
    if ball.xcor() > 400:
        ball.reset_pos()
        score.l_point()
    
    if ball.xcor() < -400:
        ball.reset_pos()
        score.r_point()

screen.exitonclick()