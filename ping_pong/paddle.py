from turtle import Turtle



class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.penup()

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def up(self):
        ycor = self.ycor() + 20
        self.goto(x=350, y=ycor)

    def down(self):
        ycor = self.ycor() - 20
        self.goto(x=350, y=ycor)

    def w_key(self):
        ycor = self.ycor() + 20
        self.goto(x=-350, y=ycor)

    def s_key(self):
        ycor = self.ycor() - 20
        self.goto(x=-350, y=ycor)


