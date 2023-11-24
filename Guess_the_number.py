#Program of the day guess the number
import random
number = random.randint(1, 100)

print("I'm thinking of a number between 1 and 100. Can you guess what it is?")

while True:
    guess = int(input("Enter your guess: "))
    
    if guess < number:
        print("Too low! Guess again.")
    elif guess > number:
        print("Too high! Guess again.")
    else:
        print("Congratulations! You guessed the number!")
        break
