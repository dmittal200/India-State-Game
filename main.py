import turtle
import pandas


screen = turtle.Screen()
screen.title("Indian States Game")
image = "India-state.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("states_data.csv")


all_states = data.state.to_list()
states_guessed = []

while len(states_guessed)<12:
    answer_state = screen.textinput(title=f"{len(states_guessed)}/12 States",prompt="Write the state name ( You can write exit to end the game )").title()

    if answer_state == "Exit":
        break

#check if entered state is valid
    if answer_state in all_states:
        states_guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_dt = data[data.state == answer_state]
        t.goto(int(state_dt.x), int(state_dt.y))
        t.write(state_dt.state.item())
        print(state_dt.state)



# turtle.mainloop()
# screen.exitonclick()
