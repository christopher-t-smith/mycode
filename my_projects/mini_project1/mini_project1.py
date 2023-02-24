#!/usr/bin/python3
"""Mini Project #1 | Main Menu"""

# Import Game Files
import rock_paper_scissors
import tic_tac_toe

# Function to clear Console
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to get user's name
def get_name():
    player_name = input("What is your name? ")
    return player_name

# Game Choice
def game_choice():
    clear()
    print("Select a game:")
    print("1. Rock, Paper, Scissors")
    print("2. Tic-Tac-Toe")
    print("3. Quit Application")
    choice = input("Enter your choice (1-3) ")
    return choice

# Main Function to start application
def main():

    # Get the user's name
    player_name = get_name()
    
    while True:

        # Run function to get user's choic of game
        choice = game_choice()

        # Start game or quit game depending on user's choice
        if choice == "1":
            print("Starting Rock, Paper, Scissors")
            rock_paper_scissors.play(player_name)
        elif choice == "2":
            print("Starting Tic-Tac-Toe")
            tic_tac_toe.play(player_name)
        elif choice == "3":
            print("Thank you for playing!")
            return
        else:
            print("Invalid choice")

# call the main function
if __name__ == "__main__":
    main()
