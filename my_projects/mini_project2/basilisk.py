#!/usr/bin/python3
"""Basilisk Class | Christopher T. Smith"""

from items import GreatAxe
from items import SteelArmor

class Basilisk:
    def __init__(self):
        self.name = "Basilisk"
        self.max_hp = 100
        self.hp = self.max_hp
        self.attack = 50

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
            player.add_to_inventory(SteelArmor())
            player.add_to_inventory(GreatAxe())
            print("You have received a GreatAxe and Steel Armor!")