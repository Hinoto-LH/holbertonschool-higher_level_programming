#!/usr/bin/python3
"""
Module qui définit la classe Rectangle,
héritant de BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Classe Rectangle qui hérite de BaseGeometry.

    Attributs privés:
        __width (int): largeur du rectangle
        __height (int): hauteur du rectangle
    """

    def __init__(self, width, height):
        """
        Initialise un rectangle avec largeur et hauteur.

        Args:
            width (int): largeur du rectangle (>0)
            height (int): hauteur du rectangle (>0)

        Utilise integer_validator de BaseGeometry pour valider les valeurs.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calcule et retourne l'aire du rectangle.

        Returns:
            int: aire du rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Retourne la représentation en chaîne du rectangle.

        Returns:
            str: format "[Rectangle] <width>/<height>"
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
