#!/usr/bin/env python3

def main():
    usr_name = input("Please enter your name:\n>")

    usr_name = usr_name.title()
    usr_date = int(input("Please enter your birth year in YYYY format, e.g 2010:\n>"))

    sign = usr_date % 12
    zodiac = {
        "Monkey": {
            "trait": "sharp, smart, curious, and mischievous."
        },
        "Rooster": {
            "trait": "hardworking, resourceful, courageous, and talented."
        },
        "Dog": {
            "trait": "loyal, honest, cautious, and kind."
        },
        "Pig": {
            "trait": "wealth, honesty, and practicality."
        },
        "Rat": {
            "trait": "artistic, sociable, industrious, charming, and intelligent."
        },
        "Ox": {
            "trait": "strong, thorough, determined, loyal, and reliable."
        },
        "Tiger": {
            "trait": "courageous, enthusiastic, confident, charismatic, and a leader"
        },
        "Rabbit": {
            "trait": "vigilant, witty, quick-minded, and ingenious."
        },
        "Dragon": {
            "trait": "talented, powerful, lucky, and successful."
        },
        "Snake": {
            "trait": "wise, like to work alone, and determined."
        },
        "Horse": {
            "trait": "animated, active, and energetic."
        },
        "Sheep": {
            "trait": "creative, resilient, gentle, mild-mannered, and shy."
        }
    }
    
    print(f"{usr_name}, your zodiac sign is {list(zodiac.keys())[sign]}, you are {zodiac[list(zodiac.keys())[sign]]['trait']}")

main()

