from turtle import Screen, Turtle
from ball import Ball
from paddle import Paddle
from scoreboard_pong import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

sleep_duration = 0.1

def decrease_sleep_duration(duration):
    return duration / 2


while True:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()
        sleep_duration = decrease_sleep_duration(sleep_duration)

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
        sleep_duration = decrease_sleep_duration(sleep_duration)

screen.exitonclick()