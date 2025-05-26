from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore = 0
        self.rscore = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.drawline()
        self.goto(-100, 180)
        self.write(self.lscore, align=ALIGN, font=FONT)
        self.goto(100, 180)
        self.write(self.rscore, align=ALIGN, font=FONT)


    def lpoint(self):
        self.lscore += 1

        self.updatescore()

    def rpoint(self):
        self.rscore += 1

        self.updatescore()

    def drawline(self):
        self.goto(0, 300)
        self.setheading(270)
        for i in range(20):
            self.pendown()
            self.pensize(5)
            self.forward(20)
            self.penup()
            self.forward(20)
