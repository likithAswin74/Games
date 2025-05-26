from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 20, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 250)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"score = {self.score} Highscore = {self.high_score}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", 'w') as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()


    # def gameover(self):
    #     self.color("white")
    #     self.goto(0, 0)
    #     self.write("Game over", align=ALIGN, font=FONT)