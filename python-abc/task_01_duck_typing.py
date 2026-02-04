#!/usr/bin/python3
"""
Module qui définit des formes géométriques avec calcul d'aire et de périmètre.
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Classe abstraite représentant une forme géométrique.
    """

    @abstractmethod
    def area(self):
        """
        Méthode abstraite pour calculer l'aire.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Méthode abstraite pour calculer le périmètre.
        """
        pass


class Circle(Shape):
    """
    Classe représentant un cercle.
    """

    def __init__(self, radius):
        """
        Initialise un cercle avec un rayon.

        Args:
            radius (float): rayon du cercle
        """
        self.radius = radius

    def area(self):
        """
        Calcule l'aire du cercle.

        Returns:
            float: aire du cercle
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calcule le périmètre du cercle.

        Returns:
            float: périmètre du cercle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Classe représentant un rectangle.
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec largeur et hauteur.

        Args:
            width (float): largeur
            height (float): hauteur
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calcule l'aire du rectangle.

        Returns:
            float: aire du rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calcule le périmètre du rectangle.

        Returns:
            float: périmètre du rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Affiche l'aire et le périmètre d'une forme géométrique.

    Args:
        shape (Shape): instance d'une classe héritant de Shape
    """
    print("area:", shape.area())
    print("perimeter:", shape.perimeter())
