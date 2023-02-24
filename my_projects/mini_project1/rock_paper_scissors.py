#!/usr/bin/python3
"""Mini Project #1 | Rock Paper Scissors"""

# Import modules
import random
import os

# Function to clear Console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def play(player_name):
    
    clear()

    # Counter for Wins, Losses, and Ties
    wins = 0
    losses = 0
    ties = 0

    # While Loops for in game
    while True:

        # Print scoreboard
        print(f"{player_name}, Wins: {wins}, Losses: {losses}, Ties: {ties}\n")

        # Player's input for Rock, Paper, and Scissors
        player_choice = input("Please choose Rock, Paper, or Scissors: ")

        # Randomize computer's choice of Rock, Paper, or Scissors
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        # Error for if user submits inputs choice other than Rock, Paper or Scissors
        if player_choice not in ["Rock", "Paper", "Scissors"]:
            clear()
            print("Invalid choice. Please choose between Rock, Paper, or Scissors\n")
            continue

        # Print what player and computer chose
        print(f"\n{player_name} chose {player_choice}.")
        print(f"Computer chose {computer_choice}.\n")

        # Combinations between User and Computer choices
        if player_choice == computer_choice:
            print("It is a tie!")
            ties += 1

        elif (player_choice == "Rock" and computer_choice == "Scissors") or (player_choice == "Scissors" and computer_choice == "Rock") or (player_choice == "Paper" and computer_choice == "Rock"):
            print("You win!")
            wins += 1

        else:
            print ("You lose!")
            losses += 1

        # Game Quit
        choice = input("\nDo you want to play again? (y/n): ").lower()
        if choice != "y":
            clear()
            return

        else:
            clear()
