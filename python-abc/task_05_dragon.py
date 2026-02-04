#!/usr/bin/env python3
"""
Module illustrant l'utilisation des mixins en Python
avec une classe Dragon qui peut nager et voler.
"""


class SwimMixin:
    """Mixin qui ajoute la capacité de nager."""

    def swim(self):
        """Affiche que la créature nage."""
        print("The creature swims!")


class FlyMixin:
    """Mixin qui ajoute la capacité de voler."""

    def fly(self):
        """Affiche que la créature vole."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Classe Dragon qui peut nager et voler."""

    def roar(self):
        """Affiche le rugissement du dragon."""
        print("The dragon roars!")


draco = Dragon()
draco.swim
draco.fly
draco.roar
