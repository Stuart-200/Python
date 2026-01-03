import tkinter as tk
import random

window = tk.Tk()
window.title("Rock paper scissors")
window.geometry("400x300")

title = tk.Label(window, text="Rock Paper Scissors", font=("Arial", 20))
title.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=15)

computer = tk.Label(window, text="", font=("Arial", 14))
computer.pack(pady=15)

choices = ["Rock", "Paper", "Scissors"]


def play(user_choice):
    computer_choice = random.choice(choices)

    computer.config(text=f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        result_label.config(text="It's a draw!")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors")
        or (user_choice == "Paper" and computer_choice == "Rock")
        or (user_choice == "Scissors" and computer_choice == "Paper")
    ):
          result_label.config(text="You win!")

    else:
        result = "You lose!"

        result_label.config(text=result)


rock_btn = tk.Button(
    window, text="Rock🪨", font=("Arial", 14), command=lambda: play("Rock")
)
rock_btn.pack(pady=5)

paper_btn = tk.Button(
    window, text="Paper📄", font=("Arial", 14), command=lambda: play("Paper")
)
paper_btn.pack(pady=5)

scissors_btn = tk.Button(
    window, text="Scissors✂️", font=("Arial", 14), command=lambda: play("Scissors")
)
scissors_btn.pack(pady=5)

window.mainloop()
