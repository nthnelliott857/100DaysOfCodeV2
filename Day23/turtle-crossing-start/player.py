import turtle
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.shape("turtle")
        self.setheading(90)
        self.can_move = True
        self.reset()

    def up(self):
        if self.can_move:
            self.sety(self.ycor() + MOVE_DISTANCE)

    def has_reached_finish(self):
        return self.ycor() == FINISH_LINE_Y

    def reset(self):
        self.goto(STARTING_POSITION)

    def game_over(self):
        self.can_move = False

