from tkinter import *
from answer import Answer
from tkinter import messagebox
from PIL import Image, ImageTk

sol = Answer()
class UserInterFace(Tk):
    def __init__(self):
        super().__init__()
        self.user_points = 0
        self.computer_points = 0

        self.geometry("400x450")
        self.title("rock paper scissor")
        self.config(bg="pink")
        self.head = Label(text="rock paper scissor", font=("Arial", 20, "italic", "bold"), padx=80, pady=20, bg="pink")
        self.head.grid(row=0, column=0, columnspan=3)

        self.user_score = Label(text=f"score:{self.user_points}/10", font=("Arial", 10, "italic", "bold"), bg="pink")
        self.user_score.grid(row=1, column=0)

        self.computer_score = Label(text=f"score:{self.computer_points}/10", font=("Arial", 10, "italic", "bold"), bg="pink")
        self.computer_score.grid(row=1, column=2)

        self.user_label = Label(text="you", font=("Arial", 10, "italic", "bold"), pady=30, bg="pink")
        self.user_label.grid(row=2, column=0)

        self.computer_label = Label(text="computer", font=("Arial", 10, "italic", "bold"), pady=30, bg="pink")
        self.computer_label.grid(row=2, column=2)

        self.user_canvas = Canvas(width=150, height=100, bg="white")
        self.user_canvas.grid(row=3, column=0)

        self.computer_canvas = Canvas(width=150, height=100, bg="white")
        self.computer_canvas.grid(row=3, column=2)

        self.rock = Button(text="rock", font=("Arial", 10, "italic", "bold"), width=10, pady=5, command=lambda: self.solution(0))
        self.rock.grid(row=4, column=0, pady=10)

        self.paper = Button(text="paper", font=("Arial", 10, "italic", "bold"), width=10, pady=5, command=lambda: self.solution(1))
        self.paper.grid(row=5, column=0, pady=5)

        self.scissor = Button(text="scissor", font=("Arial", 10, "italic", "bold"), width=10, pady=5, command=lambda: self.solution(2))
        self.scissor.grid(row=6, column=0, pady=10)

        self.play_again = Button(text="play again", font=("Arial", 10, "italic", "bold"), pady=5, command=self.play_again)
        self.play_again.grid(row=5, column=2)


    def solution(self, value):
        # it checks the answers and return who won either user or computer and this answer is stored in the answer variable
        answer = sol.check_answer(value)

        #  if computer and user points touches 10, declaring the winner who has higher score
        if self.user_points == 10:
            messagebox.showinfo(title="game over", message="game over , you won the game ")

        elif self.computer_points == 10:
            messagebox.showinfo(title="game over", message="game over , computer won the game you lose")

        else:
            # getting what image has to put on the user_canvas widget and changes the images by calling the change_user_image function
            user_image = sol.get_user_image()
            self.change_user_image(user_image)

            # getting what image has to put on the computer_image and changes the image by calling the change_computer_image function
            computer_image = sol.get_computer_image()
            self.change_computer_image(computer_image)

            # checking and increasing the points who won
            if answer == "user":
                self.user_points += 1
                self.user_score.config(text=f"score:{self.user_points}/10")
            elif answer == "computer":
                self.computer_points += 1
                self.computer_score.config(text=f"score:{self.computer_points}/10")
            else:
                pass

    # if user clicks the play again button everything is restarted
    def play_again(self):
        self.user_points = 0
        self.computer_points = 0
        self.user_score.config(text=f"score:{self.user_points}/10")
        self.computer_score.config(text=f"score:{self.computer_points}/10")
        self.user_canvas.config()

        self.user_canvas = Canvas(width=150, height=100, bg="white")
        self.user_canvas.grid(row=3, column=0)

        self.computer_canvas = Canvas(width=150, height=100, bg="white")
        self.computer_canvas.grid(row=3, column=2)

    # function to change the canvas image of the computer
    def change_user_image(self, image_name):
        pil_image = Image.open(image_name)
        self.tk_image_user = ImageTk.PhotoImage(pil_image)
        self.user_canvas.create_image(80, 50, image=self.tk_image_user)

    # function to change the user image of the user
    def change_computer_image(self, image_name):
        pil_image = Image.open(image_name)
        self.tk_image_computer = ImageTk.PhotoImage(pil_image)
        self.computer_canvas.create_image(80, 50, image=self.tk_image_computer)

obj = UserInterFace()
obj.mainloop()
