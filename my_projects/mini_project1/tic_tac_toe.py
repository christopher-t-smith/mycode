#!/usr/bin/python3
"""Mini Project #1 | Tic-Tac-Toe"""

# Import Modules
import os
import random

# Clear Console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Board for tic-tac-toe game
def print_board(board):
    print("   |   |")
    print(" {} | {} | {}".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |")
    print(" {} | {} | {}".format(board[3], board[4], board[5]))
    print("___|___|___")
    print("   |   |")
    print(" {} | {} | {}".format(board[6], board[7], board[8]))
    print("   |   |")

# Player's turn
def get_player_move(board):
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move) - 1] == ' ':
            return int(move) - 1
        else:
            print("Invalid move, please try again.")

# Computer's turn
def get_computer_move(board):
    empty_squares = [i for i in range(9) if board[i] == ' ']
    return random.choice(empty_squares)
            

# Winning possibilities
def check_win(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
   
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
   
    if ' ' not in board:
       return 'tie'
    return None

def play(player_name):
    wins = 0
    losses = 0
    ties = 0

    while True:

        board = [' '] * 9
        player = 'X'
        computer = 'O'
        clear()
        print_board(board)

        while True:

            # Print scoreboard
            print(f"\n{player_name}, Wins: {wins}, Losses: {losses}, Ties: {ties}\n")

            move = get_player_move(board)
            board[move] = player
            clear()
            print_board(board)
            winner = check_win(board)
            if winner:
                break

            move = get_computer_move(board)
            board[move] = computer
            clear()
            print_board(board)
            winner = check_win(board)
            if winner:
                break

        if winner == 'X':
            print("{} wins!".format(player_name))
            wins += 1
        elif winner == 'O':
            print("Computer wins!")
            losses += 1
        else:
            print("Tie game.")
            ties += 1

        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() != 'y':
            break

    print("Wins: {}\nLosses: {}\nTies: {}".format(wins, losses, ties))

