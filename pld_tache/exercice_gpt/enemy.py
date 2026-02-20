#!/usr/bin/python3
from character import Character


class Enemy(Character):
    def __init__(self, name, hp, damage):
        super().__init__(name, hp)
        self._damage = damage

    def attack(self):
        return self._damage

    def take_damage(self, damage):
        self._hp -= damage
        if self._hp < 0:
            self._hp = 0
