import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors")

        self.user_choice_label = tk.Label(master, text="Your Choice:")
        self.user_choice_label.grid(row=0, column=0, padx=5, pady=5)

        self.computer_choice_label = tk.Label(master, text="Computer's Choice:")
        self.computer_choice_label.grid(row=1, column=0, padx=5, pady=5)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.play_button = tk.Button(master, text="Play", command=self.play)
        self.play_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def play(self):
        user_choice = self.get_user_choice()
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        
        self.user_choice_label.config(text=f"Your Choice: {user_choice}")
        self.computer_choice_label.config(text=f"Computer's Choice: {computer_choice}")

        result = self.determine_winner(user_choice, computer_choice)
        self.result_label.config(text=result)

    def get_user_choice(self):
        user_choice_window = tk.Toplevel(self.master)
        user_choice_window.title("Your Choice")
        
        choice_var = tk.StringVar(user_choice_window)
        choice_var.set("Rock")

        choice_label = tk.Label(user_choice_window, text="Select your choice:")
        choice_label.pack(padx=5, pady=5)

        choices = ["Rock", "Paper", "Scissors"]
        choice_menu = tk.OptionMenu(user_choice_window, choice_var, *choices)
        choice_menu.pack(padx=5, pady=5)

        confirm_button = tk.Button(user_choice_window, text="Confirm", command=lambda: user_choice_window.destroy())
        confirm_button.pack(padx=5, pady=5)

        user_choice_window.focus_set()
        user_choice_window.grab_set()
        user_choice_window.wait_window()

        return choice_var.get()

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Scissors" and computer_choice == "Paper") or \
             (user_choice == "Paper" and computer_choice == "Rock"):
            return "Congratulations! You win!"
        else:
            return "Sorry! You lose."

def main():
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
