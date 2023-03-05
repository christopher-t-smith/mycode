#!/usr/bin/python3
"""Mini-Project 2: Dungeon Crawler | Christopher T. Smith"""

import sys
import os
from rooms import Rooms

from character import Player

player = Player()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def showInstructions():
    clear()
    """Show the game instructions when called"""
    #print a main menu and the commands
    print('''
    RPG Game
    ========
    Quest: Make your way through the dungeon and defeat the dragon!
    ========
    Tips:
    -Defeating monsters drop potions. Defeating bosses drops equipment.
    -Manage the use of your potions. Gather what you can before attempting a boss.
    -Total of 5 Floors (current_floor x 2 = amount_of_rooms).
    -Map out the dungeon so you don't get lost.
    -Have fun with the game!
    ========
    Commands:
        >go [direction]
        >equip [weapon] or equip [armor]
        >unequip [weapon] or unequip [armor]
        >use [item]
    ''')

def showStatus(Player):
    """determine the current status of the Player"""
    # Print the Player's current location
    print('---------------------------')
    print("You are currently on {} in {}".format( currentFloor, currentRoom,))
    # Print the Player's current stats and equipped items
    print(f'HP: {player.hp}')
    print(f'Attack: {player.attack}  Defense: {player.defense}')
    print(f'Equipped Weapon: {player.equipment["weapon"]}')
    print(f'Equipped Armor: {player.equipment["armor"]}')
    print('Inventory:', [str(item) for item in player.inventory])
    print("---------------------------")

# an inventory, which is initially empty
inventory = []


currentFloor = "Floor 1"
currentRoom = "Room 1"
possible_directions = Rooms[currentFloor][currentRoom]

showInstructions()

# breaking this while loop means the game is over
while True:

    # Get user input
    move = ''
    while move == '':
        showStatus(player)
        print("Possible locations: {possible_directions}".format(possible_directions=possible_directions))
        move = input('>')

    move = move.lower().split(" ", 1)

    if move[0] == 'go':
        direction = move[1]
        if direction in Rooms[currentFloor][currentRoom]:
            currentRoom = Rooms[currentFloor][currentRoom][direction]
            clear()
        else:
            clear()
            print(f"You cannot move {move[1]}.")

    elif move[0] == 'equip':
        # Player equips an item
        item = move[1].title()
        for inventory_item in player.inventory:
            if str(inventory_item) == item:
                clear()
                inventory_item.equip(player)
                if item != 'Healing Potion':
                    print(f"You equipped {inventory_item}.")
                    break
        else:
            clear()
            print(f"{item} is invalid for to equip.")

    elif move[0] == 'unequip':
        item = move[1].title()
        for equipped_item in player.equipment:
            if item in player.equipment:
                clear()
                equipped_item.unequip(player)
                print(f"You unequipped {equipped_item}.")
                break
            else:
                clear()
                print(f"You don't have {item} in your inventory.")

    elif move[0] == 'use':
        item = move[1].title()
        for inventory_item in player.inventory:
            if str(inventory_item) == item:
                clear()
                inventory_item.use(player)
                if item == 'Healing Potion':
                    print(f"You used a {inventory_item}.")
                break
        else:
            clear()
            print(f"You don't have {item} in your inventory.")

    else:
        clear()
        print('Invalid input')

    # Update current floor if necessary
    if currentRoom =='DownStairs to Floor 1':
         currentFloor = 'Floor 1'
         currentRoom = 'Boss Room'
    elif currentRoom == 'UpStairs to Floor 2':
        currentFloor = 'Floor 2'
        currentRoom = 'Room 1'
    elif currentRoom =='DownStairs to Floor 2':
         currentFloor = 'Floor 2'
         currentRoom = 'Boss Room'
    elif currentRoom == 'UpStairs to Floor 3':
        currentFloor = 'Floor 3'
        currentRoom = 'Room 1'
    elif currentRoom =='DownStairs to Floor 3':
         currentFloor = 'Floor 3'
         currentRoom = 'Boss Room'
    elif currentRoom == 'UpStairs to Floor 4':
        currentFloor = 'Floor 4'
        currentRoom = 'Room 1'
    elif currentRoom =='DownStairs to Floor 4':
         currentFloor = 'Floor 4'
         currentRoom = 'Boss Room'
    elif currentRoom == 'UpStairs to Floor 5':
        currentFloor = 'Floor 5'
        currentRoom = 'Room 1'

    possible_directions = Rooms[currentFloor][currentRoom]

        # Check if there is a monster in the room
    if "monster" in Rooms[currentFloor][currentRoom]:
        clear()
        monster = Rooms[currentFloor][currentRoom]["monster"]
        print(f"A {monster.name} appears!")
        # Battle the monster
        while monster.is_alive() and player.is_alive():
            # Prompt the user for their action
            showStatus(player)
            print(f"{monster.name} current has {monster.hp} HP")
            action = input("Choose an action: (a)ttack, (h)ealing potion\n>")
            # Handle the player's action
            if action == "a":
                clear()
                # Player attacks
                damage = player.attack
                monster.take_damage(damage)
                print(f"\nYou attack the {monster.name} for {damage} damage.")
            elif action == "h":
                clear()
                for inventory_item in player.inventory:
                    if str(inventory_item) == "Healing Potion":
                        clear()
                        inventory_item.use(player)
                        print(f"You used a {inventory_item}.")
                        break
                else:
                    clear()
                    print(f"You don't have Healing potions in your inventory.")
            else:
                clear()
                print("Invalid action!")
                continue  # Skip the rest of the loop and start over
            # Check if the monster is defeated
            if not monster.is_alive():
                clear()
                if monster.name == "Dragon":
                    clear()
                    print("Congratulations, you defeated the dragon and won the game!")
                    sys.exit()
                else:
                    print(f"You defeated the {monster.name}!")
                    del Rooms[currentFloor][currentRoom]["monster"]
                    monster.defeat(player)
                    break
            # Monster attacks
            damage = monster.attack
            player.take_damage(damage)
            print(f"The {monster.name} attacks you for {damage} damage.")
            # Check if the player is defeated
            if not player.is_alive():
                clear()
                print("Game over! You have been defeated.")
                sys.exit()
    else:
        print('\nEmpty room')




