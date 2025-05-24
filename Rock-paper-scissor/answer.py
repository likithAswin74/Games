import random

class Answer:
    def __init__(self):
        self.lst = [0, 1, 2]
        self.rock = "C:\likith\projects\Rock paper scissor\stone.png"
        self.paper = "C:\likith\projects\Rock paper scissor\paper.png"
        self.scissor = "C:\likith\projects\Rock paper scissor\Scissor.png"
        self.user_answer = 0
        self.computer_choice = 0

    def check_answer(self, answer):
        self.computer_choice = random.choice(self.lst)
        self.user_answer = answer

        print(self.user_answer)
        print(self.computer_choice)
        if self.user_answer == 2 and self.computer_choice == 0:
            return "computer"

        elif self.computer_choice == 2 and self.user_answer == 0:
            return "user"

        elif self.user_answer > self.computer_choice:
            return "user"

        elif self.computer_choice > self.user_answer:
            return "computer"

        elif self.computer_choice == self.user_answer:
            return "draw"

    def get_user_image(self):
        if self.user_answer == 0:
            return self.rock

        elif self.user_answer == 1:
            return self.paper

        elif self.user_answer == 2:
            return self.scissor

    def get_computer_image(self):
        if self.computer_choice == 0:
            return self.rock

        elif self.computer_choice == 1:
            return self.paper

        elif self.computer_choice == 2:
            return self.scissor
