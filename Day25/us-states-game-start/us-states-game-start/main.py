import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)



turtle.shape(image)
#turtle.penup()

writer = Turtle()
writer.penup()
writer.hideturtle()


data = pandas.read_csv("50_states.csv")
total_states = 50
total_correct = 0

# x = data.loc[data["state"] == "Alaska"].index[0]
#
# print(x)
#print(data.at[x, 'x'])
#     data[data["Primary Fur Color"] == "Black"])

states = data["state"]
states = states.to_list()
guessed_states = []
#print(states)
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title=f"{total_correct}/{total_states} States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        #states_to_learn = {"state": []}
        states_to_learn = [state for state in states if state not in guessed_states]
        # for state in states:
        #     if state not in guessed_states:
        #         #states_to_learn["state"].append(state)
        #         states_to_learn.append(state)
        data2 = pandas.DataFrame(states_to_learn)
        data2.to_csv("states_to_learn_1.csv")
        break
    if answer_state in states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        # index = data.loc[data["state"] == answer_state].index[0]
        #
        # state_x = data.at[index, "x"]
        # state_y = data.at[index, "y"]
        state_data = data[data.state == answer_state]
        state_x = int(state_data.x)
        state_y = int(state_data.y)
        total_correct += 1
        #print(f"{answer_state}: {state_x}, {state_y}")
        writer.goto(state_x, state_y)
        #print(writer.position())
        # # state_y = state["y"]
        writer.write(answer_state)
        # turtle.goto(state_x, state_y)
    if total_correct == 50:
        game_is_on = False



states_to_learn = {"state": []}

for state in states:
    if state not in guessed_states:
        states_to_learn["state"].append(state)

    #print(state)

#print(states_to_learn)
data2 = pandas.DataFrame(states_to_learn)
data2.to_csv("states_to_learn.csv")

#turtle.mainloop()
#screen.exitonclick()
