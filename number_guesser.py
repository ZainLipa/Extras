# Program of the Day: Number Guessing Game

import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    attempts = 0
    while True:
        # Ask the user to guess the number
        user_guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1
        
        # Check if the guess is correct
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Play the game
print("Welcome to the Number Guessing Game!")
number_guessing_game()
