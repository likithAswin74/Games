from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def function_w():
    tim.forward(5)
def function_s():
    tim.backward(5)
def anticlockwise():
    tim.setheading(tim.heading() + 10)

def clockwise():
    tim.setheading(tim.heading() - 10)
def function_c():
    screen.resetscreen()
screen.listen()
screen.onkey(key="w", fun=function_w)
screen.onkey(key="s", fun=function_s)
screen.onkey(key="c", fun=function_c)
screen.onkey(key="a", fun=anticlockwise)
screen.onkey(key="d", fun=clockwise)

screen.exitonclick()
