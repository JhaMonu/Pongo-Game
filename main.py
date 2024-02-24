from turtle import Turtle, Screen
from Paddle import PADDLE
from scorebord import Scorebord
from ball import Ball
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

turtle = Turtle()


r_paddle = PADDLE((375, 0))
l_paddle = PADDLE((-375, 0))
ball = Ball()
scorebord = Scorebord()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() <-280:
        ball.bounce_y()


    if ball.distance(r_paddle) < 40 and ball.xcor() > 320 or ball.distance(l_paddle) < 40 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset_possotion()
        scorebord.l_point()


    elif ball.xcor() <-380:
        ball.reset_agian()
        scorebord.r_point()

screen.exitonclick()