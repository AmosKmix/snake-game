from turtle import Screen
import paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")

screen.tracer(0)  # animation turned off

pad_R = paddle.Paddle((350, 0))
pad_L = paddle.Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()

screen.onkeypress(fun=pad_R.go_up, key="Up")
screen.onkeypress(fun=pad_R.go_down, key="Down")
screen.onkeypress(fun=pad_L.go_up, key="w")
screen.onkeypress(fun=pad_L.go_down, key="s")


game_is_on = True

while game_is_on:
    # making sure the screen wont have any traces - screen must be updated all the time .
    screen.update()

    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(pad_R) < 40 or ball.xcor() < -320 and ball.distance(pad_L) < 40:
        ball.bounce_x()
        ball.speed_up()
    # Detect a goal on R side
    if ball.xcor() > 360:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()
        ball.y_move = 10
    # Detect a goal on L side
    if ball.xcor() < -360:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()
        ball.y_move = 10

    time.sleep(ball.move_speed)


screen.exitonclick()
