#!/usr/bin/python3
"""Slime Class | Christopher T. Smith"""

import random

from items import HealingPotion

class Slime:
    def __init__(self):
        self.name = "Slime"
        self.max_hp = 50
        self.hp = self.max_hp
        self.attack = random.randint(10, 15)

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
            player.add_to_inventory(HealingPotion())
            print("You have received a Healing Potion!")