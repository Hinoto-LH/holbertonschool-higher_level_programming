#!/usr/bin/python3
from character import Character


class Hero(Character):
    def __init__(self, name, hp):
        super().__init__(name, hp)
        self._level = 1  # attribut d'instance

    def level_up(self):
        self._level += 1
        return self._level
