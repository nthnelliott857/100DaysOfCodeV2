import random
from turtle import Turtle
from random import Random


class Ball(Turtle):

    def __init__(self, left_paddle, right_paddle):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.start = True
        self.last_point = ""
        self.get_heading()
        self.start = False
        print(f"heading: {self.heading()}")
        self.left_paddle = left_paddle
        self.right_paddle = right_paddle
        self.ball_speed_factor = 1

    def move(self):
        if self.is_obstructed_by_border():
            self.bounce_y()
        elif self.is_obstructed_by_paddle():
            self.bounce_x()
        if not self.is_out_of_bounds():
            self.forward(20)
        elif self.is_out_of_bounds():
            self.reset_position()


    def bounce_y(self):
        self.setheading(-1 * self.heading())

    def bounce_x(self):
        self.setheading(180 - self.heading())

    def is_obstructed_by_border(self):
        return self.ycor() > 280 or self.ycor() < -280

    def is_obstructed_by_paddle(self):
        if self.distance(self.right_paddle) < 50 and self.xcor() > 320 or self.distance(
                self.left_paddle) < 50 and self.xcor() < -320:
            print("Made contact")
            self.increase_speed()
            print(self.speed())
            return True
        else:
            return False

    def is_out_of_bounds(self):
        if self.xcor() < -400 or self.xcor() > 400:
            self.whose_point()
            return True
        else:
            return False

    def get_heading(self):
        if self.start:
            self.setheading(random.randint(0, 360))
        elif self.last_point == "R":
            self.setheading(random.randint(-90, 90))
        elif self.last_point == "L":
            self.setheading(random.randint(180, 270))

    def whose_point(self):
        if self.xcor() > 400:
            self.last_point = "L"
        elif self.xcor() < -400:
            self.last_point = "R"

    def reset_position(self):
        self.goto(0, 0)
        self.get_heading()
        self.ball_speed_factor = 1

    def get_last_point(self):
        return self.last_point

    def increase_speed(self):
        self.ball_speed_factor += 0.5
        # if self.speed() < 10:
        #     self.speed(self.speed() + 1)
        # else:
        #     self.speed("fastest")

    def get_ball_speed_factor(self):
        return self.ball_speed_factor
