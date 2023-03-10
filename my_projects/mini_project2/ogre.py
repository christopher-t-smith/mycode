#!/usr/bin/python3
"""Ogre Class | Christopher T. Smith"""

import random

from items import Dagger
from items import LeatherArmor

class Ogre:
    def __init__(self):
        self.name = "Ogre"
        self.max_hp = 30
        self.hp = self.max_hp
        self.attack = 30

    def take_damage(self, amount):
        self.hp -= random.randint(15, 25)

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
            player.add_to_inventory(Dagger())
            player.add_to_inventory(LeatherArmor())
            print("You have received a Dagger and Leather Armor!")