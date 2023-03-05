#!/usr/bin/python3
"""Character Class | Christopher T. Smith"""

class Player:
    def __init__(self):
        self.hp = 100
        self.attack = 25
        self.defense = 0
        self.inventory = []
        self.equipment = {
            "weapon": None,
            "armor": None
        }

    def attack(self, monster):
        damage = self.attack
        # ... calculate damage based on other factors (e.g. weapon, monster defense)
        monster.take_damage(damage)

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def remove_from_inventory(self, item):
        self.inventory.remove(item)


