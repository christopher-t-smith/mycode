#!/usr/bin/python3
"""Troll Class | Christopher T. Smith"""

from items import Broadsword
from items import BronzeArmor

class Troll:
    def __init__(self):
        self.name = "Troll"
        self.max_hp = 85
        self.hp = self.max_hp
        self.attack = 40

    def take_damage(self, amount):
        self.hp -= amount

    def is_alive(self):
        return self.hp > 0

    def attack_player(self, player):
        damage = self.attack - player.defense
        if damage < 0:
            damage = 0
        player.take_damage(damage)
        print("The {} attacks you for {} damage!".format(self.name, damage))

    def __str__(self):
        return self.name
    
    def defeat(self, player):
        if not self.is_alive():
            player.add_to_inventory(Broadsword())
            player.add_to_inventory(BronzeArmor())
            print("You have received a Broadsword and Bronze Armor!")