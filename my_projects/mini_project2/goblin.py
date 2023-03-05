#!/usr/bin/python3
"""Goblin Class | Christopher T. Smith"""

import random

from items import HealingPotion
class Goblin:
    def __init__(self):
        self.name = "Goblin"
        self.max_hp = 60
        self.hp = self.max_hp
        self.attack = random.randint(15, 25)

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