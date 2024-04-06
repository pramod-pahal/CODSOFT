import tkinter as tk
import random

def play_game(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    result_label.config(text=f"Computer chooses: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result_label.config(text="You win!")
    else:
        result_label.config(text="You lose!")

def play_again():
    result_label.config(text="")
    user_choice_var.set("")

root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

user_choice_var = tk.StringVar()
user_choice_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
user_choice_label.pack()

user_choice_menu = tk.OptionMenu(root, user_choice_var, "Rock", "Paper", "Scissors")
user_choice_menu.pack()

play_button = tk.Button(root, text="Play", command=lambda: play_game(user_choice_var.get()))
play_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack()

root.mainloop()
