import colorgram
import random
import turtle
from turtle import Turtle, Screen

# colors = colorgram.extract('SpotPainting04.jpg', 54)
#
#
#
# colors_list = []
#
# # colors_list.append(colors[0].rgb[0])
# # print(colors_list)
#
# for i in range(len(colors)):
#     value = colors[i].rgb
#     group = (value[0], value[1], value[2])
#     colors_list.append(group)

timmy_the_turtle = Turtle()
timmy_the_turtle.penup()
timmy_the_turtle.hideturtle()
timmy_the_turtle.speed("fastest")
turtle.colormode(255)
color_list = [(230, 215, 101),(234, 246, 242), (154, 80, 38), (244, 231, 236), (207, 159, 105), (181, 175, 18), (108, 165, 210), (25, 91, 160), (106, 176, 124), (194, 91, 105), (13, 37, 97), (72, 43, 23), (50, 121, 23), (187, 133, 150), (94, 192, 47), (106, 32, 54), (195, 94, 75), (25, 97, 25), (100, 120, 169), (180, 206, 170), (250, 169, 173), (24, 53, 110), (251, 171, 163), (149, 191, 244), (104, 60, 18), (81, 30, 46), (132, 79, 90), (18, 75, 105), (91, 153, 156), (45, 49, 45), (104, 52, 26), (161, 202, 213), (213, 203, 31)]



print(color_list)

timmy_the_turtle.sety(-50)
timmy_the_turtle.setx(-100)



for i in range(10):
    for j in range(10):
        timmy_the_turtle.color(random.choice(color_list))
        timmy_the_turtle.dot(20)
        timmy_the_turtle.forward(50)
    timmy_the_turtle.setx(-100)
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(50)
    timmy_the_turtle.right(90)
    # timmy_the_turtle.right(180)
    # timmy_the_turtle.home()
    # timmy_the_turtle.left(90)
    # timmy_the_turtle.forward(50)
    # timmy_the_turtle.right(90)

#timmy_the_turtle.forward(455)

# 20 + 50 + 20 + 50 + 20 + 50 + 20 + 50 + 20 + 50 + 20 + 50 + 20/2 + 50/2 = 455




screen = Screen()
screen.exitonclick()


# 20 in size
# 50 apart
# 10 x 10

