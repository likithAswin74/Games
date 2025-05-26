import turtle
import random

screen = turtle.Screen()
screen.setup(width=500, height=400)
userbet = screen.textinput(title="bet a turtle", prompt="enter the colour of the turtle")
colors = ["red", "yellow", "orange", "green", "blue", "purple"]
y = [-70, -40, -10, 20, 50, 80]
is_true = False
turtle_list = []
for turtle_index in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y[turtle_index])
    turtle_list.append(new_turtle)


if userbet:
    is_true = True

while is_true:

    for turtle in turtle_list:
        if turtle.xcor() > 220:
            is_true = False
            winning_color = turtle.pencolor()
            if winning_color == userbet:
                print(f"you win.  {winning_color} is the winner")
            else:
                print(f"you lost. {winning_color} is the winner")


        value = random.randint(0, 10)
        turtle.forward(value)



screen.exitonclick()