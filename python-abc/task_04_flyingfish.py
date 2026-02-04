#!/usr/bin/python3
"""
Module qui définit des classes pour illustrer le multiple héritage:
Fish, Bird et FlyingFish.
"""


class Fish:
    """
    Classe représentant un poisson.
    """

    def swim(self):
        """Affiche que le poisson nage."""
        print("The fish is swimming")

    def habitat(self):
        """Affiche l'habitat du poisson."""
        print("The fish lives in water")


class Bird:
    """
    Classe représentant un oiseau.
    """

    def fly(self):
        """Affiche que l'oiseau vole."""
        print("The bird is flying")

    def habitat(self):
        """Affiche l'habitat de l'oiseau."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Classe représentant un poisson volant,
    héritant de Fish et Bird.
    """

    def fly(self):
        """Affiche que le poisson volant vole."""
        print("The flying fish is soaring!")

    def swim(self):
        """Affiche que le poisson volant nage."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Affiche que le poisson volant vit dans l'eau et le ciel."""
        print("The flying fish lives both in water and the sky!")


Magicarpe = FlyingFish()
Magicarpe.fly
Magicarpe.swim
Magicarpe.habitat
mro = FlyingFish.__mro__
