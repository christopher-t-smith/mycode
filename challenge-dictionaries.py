#!/usr/bin/env python3
"""Challenge: Dictionaries """


def main():

    marvelchars= {
    "Starlord":
        {"real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"},

    "Mystique":
        {"real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"},

    "Hulk":
        {"real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"}
    }


    valid_keys = {k.lower(): [sk.lower() for sk in v.keys()] for k,v in marvelchars.items()}

    while True:

        char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk) ")

        if char_name not in marvelchars:
            print("Invalid character name. Please try again.")
            continue # Start over with another iterations of the while loop

        char_stat = input("What statistic do you want to know about? (real name, powers, archenemy) ")

        if char_stat not in marvelchars[char_name]:
            print("Invalid statistic name. Please try again. ")
            continue # Start over with another iteration of the while loop

        value = marvelchars[char_name][char_stat]

        if char_stat == "real name":
            value = value.title() # Capitalize the first letter of each word in the real name

        print(f"{char_name}'s {char_stat} is: {value}")
        again = input("Do you want to try again? (y/n) ")
        if again.lower() != "y":
            break # Exit the while loop and end the script
main()
