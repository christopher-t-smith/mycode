# Create an application for rock paper scissors
# Keep track of Wins, losses, and ties
# Choices of rock, paper, and scissors
# Print what the player and computer selected
# User choice of quiting game after each match
# Catch errors for invalid choice

#!/usr/bin/python3
"""Mini Project #1 | Rock Paper Scissors"""

# Import random from Python Library
import random

def play(player_name):
    
    # Counter for Wins, Losses, and Ties
    wins = 0
    losses = 0
    ties = 0
    games_played = 0

    # While Loops for in game
    while True:

        # Print scoreboard
        print(f"\n{player_name}, Wins: {wins}, Losses: {losses}, Ties: {ties}")

        # Player's input for Rock, Paper, and Scissors
        player_choice = input("Please choose Rock, Paper, or Scissors: ")

        # Randomize computer's choice of Rock, Paper, or Scissors
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])

        # Error for if user submits inputs choice other than Rock, Paper or Scissors
        if player_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice. Please choose between Rock, Paper, or Scissors")
            continue

        # Print what player and computer chose
        print(f"{player_name} chose {player_choice}.")
        print(f"Computer chose {computer_choice}.")

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

        games_played += 1

        # Game Quit
        choice = input("Do you want to play again? (y/n): ").lower()
        if choice != "y":

            # Print Final Score when quitting game
            print(f"\nFinal score for {player_name}: Wins: {wins}, Losses: {losses}, Ties: {ties}")

            if wins > losses:
                print(f"{player_name} wins the game!")
            elif wins < losses:
                print("Computer loses the game!")
            else:
                print("The game is tied!")
            print("Going back to the main menu")
            return          
            
