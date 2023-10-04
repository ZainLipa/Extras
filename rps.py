# Program of the Day: Rock, Paper, Scissors Game

import random

def play_rock_paper_scissors():
    # Define the choices
    choices = ["rock", "paper", "scissors"]

    # Get user's choice
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Validate user's choice
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return

    # Generate a random choice for the computer
    computer_choice = random.choice(choices)

    # Determine the winner
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    # Display the results
    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")
    print(result)

# Play the game
play_rock_paper_scissors()
