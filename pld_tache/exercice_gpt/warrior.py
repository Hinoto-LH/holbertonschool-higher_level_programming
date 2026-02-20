#!/usr/bin/python3
from hero import Hero


class Warrior(Hero):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self._strength = strength

    def attack(self):
        return self._strength * self._level

    def take_damage(self, damage):
        reduced_damage = damage * 0.8
        self._hp -= reduced_damage
        if self._hp < 0:
            self._hp = 0
