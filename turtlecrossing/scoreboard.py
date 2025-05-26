from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGN = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.penup()
        self.goto(-280, 260)
        self.write(f"level = {self.level}", align="left", font=FONT)


    def gameover(self):
        self.goto(0, 0)
        self.write("Game over", align=ALIGN, font=FONT)


