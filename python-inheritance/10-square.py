#!/usr/bin/python3
"""
Module qui définit la classe Square,
héritant de Rectangle.
"""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """
    Classe Square qui hérite de Rectangle.

    Attribut privé:
        __size (int): taille du carré
    """

    def __init__(self, size):
        """
        Initialise un carré avec une taille.

        Args:
            size (int): taille du carré (>0)

        Utilise integer_validator de BaseGeometry pour valider la valeur.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size__ = size
