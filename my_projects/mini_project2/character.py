#!/usr/bin/python3
"""Character Class | Christopher T. Smith"""

class Character:
    def __init__(self):
        self.hp = 100
        self.mp = 30
        self.attack = 25
        self.defense = 0
        self.inventory = []
        self.equipment = {
            "weapon": None,
            "armor": None
        }

    def show_status(self):
        print(f"HP: {self.hp}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Iventory: {self.inventory}")

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= damage

    def add_to_inventory(self, item):
        self.inventory.append(item)


