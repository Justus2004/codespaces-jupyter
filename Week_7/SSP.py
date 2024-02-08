import tkinter as tk
from tkinter import messagebox
import random

def get_user_choice():
    user_choice = user_input.get().strip().lower()
    while user_choice not in ['schere', 'stein', 'papier']:
        messagebox.showinfo("Ungültige Eingabe", "Bitte wähle Schere, Stein oder Papier.")
        return
    play_game(user_choice)

def get_computer_choice():
    return random.choice(['schere', 'stein', 'papier'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Unentschieden"
    elif (user_choice == 'schere' and computer_choice == 'papier') or \
         (user_choice == 'stein' and computer_choice == 'schere') or \
         (user_choice == 'papier' and computer_choice == 'stein'):
        return "Du gewinnst!"
    else:
        return "Der Computer gewinnt!"

def play_game(user_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(user_choice, computer_choice)
    messagebox.showinfo("Ergebnis", f"Du hast {user_choice} gewählt. Der Computer hat {computer_choice} gewählt.\n{result}")

root = tk.Tk()
root.title("Schere-Stein-Papier")

user_input_label = tk.Label(root, text="Wähle Schere, Stein oder Papier:")
user_input_label.pack()
user_input = tk.Entry(root)
user_input.pack()

play_button = tk.Button(root, text="Spiel starten", command=get_user_choice)
play_button.pack()

root.mainloop()
