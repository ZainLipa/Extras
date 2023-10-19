#Program of the Day: Text-Based Adventure Game
def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a mysterious forest. You can go north or south.")

    while True:
        choice = input("What direction do you choose? (north/south/quit): ").lower()

        if choice == "north":
            print("You venture deeper into the forest and discover a hidden treasure!")
            print("Congratulations, you win!")
            break
        elif choice == "south":
            print("You encounter a wild bear and run away in fear.")
        elif choice == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 'north', 'south', or 'quit'.")

# Start the game
start_game()
