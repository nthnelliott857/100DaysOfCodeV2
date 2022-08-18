import random
import turtle
from turtle import Turtle, Screen
from random import Random

def right_square(length):
    timmy_the_turtle.forward(length)
    timmy_the_turtle.right(90)

def left_square(length):
    timmy_the_turtle.forward(length)
    timmy_the_turtle.left(90)

#steps = int(input("How many steps should the random_walk consist of? "))

gap_size = input("What's the gap size? ")

timmy_the_turtle = Turtle()
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("red")

colors = ["orange", "green", "black", "blue", "yellow", "green", "grey", "purple", "red", "brown", "cyan", "gray", "gold", "pink"]

timmy_the_turtle.speed("fastest")


turtle.colormode(255)



def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)


def draw_spirograph(size_of_gap):
    for i in range(int(360/int(size_of_gap))):
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + float(size_of_gap))



draw_spirograph(gap_size)



screen = Screen()
screen.exitonclick()




# while go:
#     timmy_the_turtle.color(random_color())
#     direction = random.randint(0,3)
#     if direction == 1:
#         timmy_the_turtle.right(90)
#     elif direction == 1:
#         timmy_the_turtle.right(180)
#     elif direction == 2:
#         timmy_the_turtle.right(270)
#
#     timmy_the_turtle.forward(30)

















# for i in range(3,11):
#     timmy_the_turtle.pencolor(random.choice(colors))
#     for j in range(0, i):
#         angle = 360/i
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)









# for i in range(100):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(5)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(5)



# timmy_the_turtle.left(180)
# right_square(100)
# right_square(100)
# right_square(100)
# timmy_the_turtle.forward(100)


















