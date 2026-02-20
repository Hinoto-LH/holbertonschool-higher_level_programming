#!/usr/bin/python3
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def take_damage(self, damage):
        pass

    def is_alive(self):
        return self._hp > 0
