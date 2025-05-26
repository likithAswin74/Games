from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xvalue = 10
        self.yvalue = 10
        self.move_speed = 0.1
    # def move(self):
    #     self.setheading(35)
    #     self.forward(20)
    def move(self):
        x = self.xcor() + self.xvalue
        y = self.ycor() + self.yvalue
        self.goto(x, y)
        # print(self.xcor)
        # print(self.yvalue)

    def bounce_y(self):
        self.yvalue *= -1


    def bounce(self):
        self.xvalue *= -1
        self.move_speed *= 0.9



    def restart(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce()
