#!/usr/bin/python3
from hero import Hero


class Mage(Hero):
    def __init__(self, name, hp, mana):
        super().__init__(name, hp)
        self._mana = mana

    def attack(self):
        return self._mana + (self._level * 5)

    def take_damage(self, damage):
        self._hp -= damage
        if self._hp < 0:
            self._hp = 0
