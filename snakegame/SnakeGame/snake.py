from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
SQUARE_SIZE = 20


class Snake:

    def __init__(self, size):
        self.segments = []
        self.size = size
        self.create_snake(size)
        self.head = self.segments[0]

    def create_snake(self, size):
        for i in range(0, size):
            self.add_segment(xpos=-i * SQUARE_SIZE, ypos=0)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def add_segment(self, xpos, ypos):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(xpos, ypos)
        self.segments.append(segment)

    def extend(self):
        # add a new segment to the snake
        self.add_segment(xpos=self.segments[-1].xcor(), ypos=self.segments[-1].ycor())

    def left(self):
        if self.head.heading() != RIGHT:
            self.segments[0].seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.segments[0].seth(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.segments[0].seth(DOWN)
