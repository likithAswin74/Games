import turtle
import pandas
screen = turtle.Screen()
screen.title("India states game")
image = "India-states.gif"
screen.addshape(image)
turtle.shape(image)
# def keepval(x, y):
#     print(x, y)
#
# turtle.onscreenclick(keepval)
# turtle.mainloop()
data = pandas.read_csv("data.csv")
all_states = data["State"].to_list()
guess_states = []
while len(guess_states) <= len(all_states):
    answer = screen.textinput(title=f"{len(guess_states)}/28 states", prompt="what's the next state").title()
    if answer == "Exit":
        missing_states = []
        for states in all_states:
            if states not in guess_states:
                missing_states.append(states)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("learnstates.csv")
        break
    if answer in all_states:
        guess_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        found_state = data[data["State"] == answer]
        t.goto(int(found_state.X.iloc[0]), int(found_state.Y.iloc[0]))
        t.pendown()
        t.write(answer)





