#!/usr/bin/python3
"""
Module qui définit une hiérarchie de classes abstraites pour les animaux.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Classe abstraite représentant un animal.
    """

    @abstractmethod
    def sound(self):
        """
        Méthode abstraite qui doit retourner le son de l'animal.

        Raises:
            NotImplementedError: si la méthode n'est pas surchargée
        """
        pass


class Dog(Animal):
    """
    Classe représentant un chien, hérite de Animal.
    """

    def sound(self):
        """
        Retourne le son du chien.

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Classe représentant un chat, hérite de Animal.
    """

    def sound(self):
        """
        Retourne le son du chat.

        Returns:
            str: "Meow"
        """
        return "Meow"
