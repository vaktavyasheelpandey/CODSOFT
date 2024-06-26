import tkinter as tk
from tkinter import messagebox
import random

# Define the choices and game logic
choices = ["Rock", "Paper", "Scissors"]

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    computer_choice = random.choice(choices)
    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    update_scores(result)

def update_scores(result):
    global user_score, computer_score
    if "win" in result:
        user_score += 1
    elif "lose" in result:
        computer_score += 1
    score_label.config(text=f"Score - You: {user_score}, Computer: {computer_score}")

def play_again():
    result_label.config(text="")
    if messagebox.askyesno("Play Again", "Do you want to play another round?"):
        pass
    else:
        root.quit()

# Initialize scores
user_score = 0
computer_score = 0

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Create and place the widgets
tk.Label(root, text="Choose Rock, Paper, or Scissors").pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", command=lambda: play_game("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", command=lambda: play_game("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", command=lambda: play_game("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", pady=10)
result_label.pack()

score_label = tk.Label(root, text=f"Score - You: {user_score}, Computer: {computer_score}", pady=10)
score_label.pack()

play_again_button = tk.Button(root, text="Play Again", command=play_again)
play_again_button.pack(pady=10)

# Run the application
root.mainloop()
