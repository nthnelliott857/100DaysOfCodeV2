from turtle import Screen, Turtle
from paddle import Paddle
import time
from ball import Ball
from scoreboard import ScoreBoard


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball(right_paddle=right_paddle, left_paddle=left_paddle)
scoreboard = ScoreBoard()
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

def get_time(time):
    return float(time/10)


game_is_on = True

while game_is_on:
    time.sleep(1/(10**ball.get_ball_speed_factor()))
    screen.update()
    ball.move()

    if ball.is_out_of_bounds():
        if ball.get_last_point() == "L":
            scoreboard.l_point()
        else:
            scoreboard.r_point()




screen.exitonclick()




