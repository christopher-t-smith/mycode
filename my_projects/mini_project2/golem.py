#!/usr/bin/python3
"""golem Class | Christopher T. Smith"""

from items import LongSword
from items import IronArmor

class Golem:
    def __init__(self):
        self.name = "Golem"
        self.max_hp = 120
        self.hp = self.max_hp
        self.attack = 30

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
            player.add_to_inventory(IronArmor())
            player.add_to_inventory(LongSword())
            print("You have received a LongSword and Iron Armor!")