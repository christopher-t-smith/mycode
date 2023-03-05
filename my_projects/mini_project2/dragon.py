#!/usr/bin/python3
"""Dragon Class | Christopher T. Smith"""

class Dragon:
    def __init__(self):
        self.name = "Dragon"
        self.max_hp = 200
        self.hp = self.max_hp
        self.attack = 70

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