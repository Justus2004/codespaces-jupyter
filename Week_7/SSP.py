import random

def get_user_choice():
    user_choice = input("Wähle Schere, Stein oder Papier: ").strip().lower()
    while user_choice not in ['schere', 'stein', 'papier']:
        print("Ungültige Eingabe. Bitte wähle Schere, Stein oder Papier.")
        user_choice = input("Wähle Schere, Stein oder Papier: ").strip().lower()
    return user_choice

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

def play_game():
    print("Willkommen beim Schere-Stein-Papier-Spiel!")
    play_again = True
    while play_again:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Du hast {user_choice} gewählt. Der Computer hat {computer_choice} gewählt.")
        print(determine_winner(user_choice, computer_choice))
        play_again_input = input("Möchtest du noch einmal spielen? (ja/nein): ").strip().lower()
        play_again = play_again_input == 'ja'

play_game()
