#!/usr/bin/env python3

import requests

def main():

    for i in range(5):
        pokenum= input("Pick a number between 1 and 151!\n>")
        pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()
    
        pokemon_name = pokeapi["name"]
        print(f"The Pokemon for number {pokenum} is {pokemon_name.capitalize()}!")

        front_default_url = pokeapi["sprites"]["front_default"]
        print(front_default_url)

        game_count = len(pokeapi["game_indices"])
        print(f"This Pokemon character has appeared in {game_count} games!")


   # print(pokeapi)

main()

