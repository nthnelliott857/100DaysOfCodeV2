import random
from turtle import Turtle, Screen
from random import Random

is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

j = 0

for i in range(0,6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230, y=-100 + j)
    j += 30
    turtles.append(turtle)

winner = ""

if user_bet:
    is_race_on = True



while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You've won! The winner was the {winner} turtle.")
            else:
                print(f"You've lost; you bet that the {user_bet} turtle would win, but the {winner} turtle won.")
        else:
            random_distance = random.randint(0,10)
            turtle.forward(random_distance)





# tim = Turtle(shape="turtle")
# tim.penup()
# tim.goto(x=-230, y=-100)

screen.exitonclick()
