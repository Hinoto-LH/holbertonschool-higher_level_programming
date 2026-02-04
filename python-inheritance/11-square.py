#!/usr/bin/python3
"""
Module qui définit la classe Square,
héritant de Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle


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

        Utilise integer_validator pour valider la valeur.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Retourne la représentation en chaîne du carré.

        Returns:
            str: format "[Square] <width>/<height>"
        """
        return f"[Square] {self.__size}/{self.__size}"
