#!/usr/bin/python3
"""Items | Christopher T. Smith"""

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class HealingPotion(Item):
    def __init__(self):
        super().__init__("Healing Potion", "Restores 50 HP")

    def use(self, player):
        player.hp = min(player.hp + 50, 100)
        player.remove_from_inventory(self)

    def equip(self, player):
        print(f"You are unable to equip {self.name}.")

    def __str__(self):
        return self.name

class Dagger(Item):
    def __init__(self):
        super().__init__("Dagger", "A small, sharp knife, +10 attack damage")

    def use(self, player):
        print(f"Invalid item to use {self.name}. Input equip.")

    def equip(self, player):
        if "weapon" in player.equipment:
            previous_weapon = player.equipment["weapon"]
            if previous_weapon:
                previous_weapon.unequip(player)
            player.equipment["weapon"] = self
            player.attack += 10
            player.remove_from_inventory(self)
        else:
            player.equipment["weapon"] = self
            player.attack += 10
            player.remove_from_inventory(self)


    def unequip(self, player):
        player.equipment["weapon"] = None
        player.attack -= 10
        player.add_to_inventory(self)

    def __str__(self):
        return self.name

class Broadsword(Item):
    def __init__(self):
        super().__init__("Broadsword", "A sturdy sword with a wide blade, +20 attack damage")

    def use(self, player):
        print(f"Invalid item to use {self.name}. Input equip.")

    def equip(self, player):
        if "weapon" in player.equipment:
            previous_weapon = player.equipment["weapon"]
            if previous_weapon:
                previous_weapon.unequip(player)
            player.equipment["weapon"] = self
            player.attack += 20
            player.remove_from_inventory(self)
        else:
            player.equipment["weapon"] = self
            player.attack += 20
            player.remove_from_inventory(self)

    def unequip(self, player):
        player.equipment["weapon"] = None
        player.attack -= 20
        player.add_to_inventory(self)

    def __str__(self):
        return self.name

class LongSword(Item):
    def __init__(self):
        super().__init__("Longsword", "A longer and heavier sword, +30 attack damage")

    def use(self, player):
        print(f"Invalid item to use {self.name}. Input equip.")

    def equip(self, player):
        if "weapon" in player.equipment:
            previous_weapon = player.equipment["weapon"]
            if previous_weapon:
                previous_weapon.unequip(player)
            player.equipment["weapon"] = self
            player.attack += 35
            player.remove_from_inventory(self)
        else:
            player.equipment["weapon"] = self
            player.attack += 35
            player.remove_from_inventory(self)

    def unequip(self, player):
        player.equipment["weapon"] = None
        player.attack -= 35
        player.add_to_inventory(self)

    def __str__(self):
        return self.name

class GreatAxe(Item):
    def __init__(self):
        super().__init__("Great Axe", "A large and powerful axe, , +40 attack damage")

    def use(self, player):
        print(f"Invalid item to use {self.name}. Input equip.")

    def equip(self, player):
        if "weapon" in player.equipment:
            previous_weapon = player.equipment["weapon"]
            if previous_weapon:
                previous_weapon.unequip(player)
            player.equipment["weapon"] = self
            player.attack += 50
            player.remove_from_inventory(self)
        else:
            player.equipment["weapon"] = self
            player.attack += 50
            player.remove_from_inventory(self)

    def unequip(self, player):
        player.equipment["weapon"] = None
        player.attack -= 50
        player.add_to_inventory(self)

    def __str__(self):
        return self.name

class LeatherArmor(Item):
    def __init__(self):
        super().__init__("Leather Armor", "Light and comfortable armor.")

    def use(self, player):
        print(f"Invalid item to use {self.name}. Input equip.")

    def equip(self, player):
        if "armor" in player.equipment:
            previous_armor = player.equipment["armor"]
            if previous_armor:
                previous_armor.unequip(player)
            player.equipment["armor"] = self
            player.defense += 10
            player.remove_from_inventory(self)

        else:
            player.equipment["armor"] = self
            player.defense += 10
            player.remove_from_inventory(self)

    def unequip(self, player):
        player.equipment["armor"] = None
        player.defense -= 10
        player.add_to_inventory(self)

    def __str__(self):
        return self.name

class BronzeArmor(Item):
    def __init__(self):
        super().__init__("Bronze Armor", "Light and thin armor.")

    def use(self, player):
        print(f"Invalid item to use {self.name}. Input equip.")

    def equip(self, player):
        if "armor" in player.equipment:
            previous_armor = player.equipment["armor"]
            if previous_armor:
                previous_armor.unequip(player)
            player.equipment["armor"] = self
            player.defense += 20
            player.remove_from_inventory(self)
        else:
            player.equipment["armor"] = self
            player.defense += 20
            player.remove_from_inventory(self)

    def unequip(self, player):
        player.equipment["armor"] = None
        player.defense -= 20
        player.add_to_inventory(self)

    def __str__(self):
        return self.name

class IronArmor(Item):
    def __init__(self):
        super().__init__("Iron Armor", "Sturdy and reliable armor.")

    def use(self, player):
        print(f"Invalid item to use {self.name}. Input equip.")

    def equip(self, player):
        if "armor" in player.equipment:
            previous_armor = player.equipment["armor"]
            if previous_armor:
                previous_armor.unequip(player)
            player.equipment["armor"] = self
            player.defense += 35
            player.remove_from_inventory(self)
        else:
            player.equipment["armor"] = self
            player.defense += 35
            player.remove_from_inventory(self)

    def unequip(self, player):
        player.equipment["armor"] = None
        player.defense -= 35
        player.add_to_inventory(self)

    def __str__(self):
        return self.name

class SteelArmor(Item):
    def __init__(self):
        super().__init__("Steel Armor", "Heavy and protective armor.")

    def use(self, player):
        print(f"Invalid item to use {self.name}. Input equip.")

    def equip(self, player):
        if "armor" in player.equipment:
            previous_armor = player.equipment["armor"]
            if previous_armor:
                previous_armor.unequip(player)
            player.equipment["armor"] = self
            player.defense += 50
            player.remove_from_inventory(self)
        else:
            player.equipment["armor"] = self
            player.defense += 50
            player.remove_from_inventory(self)

    def unequip(self, player):
        player.equipment["armor"] = None
        player.defense -= 50
        player.add_to_inventory(self)

    def __str__(self):
        return self.name