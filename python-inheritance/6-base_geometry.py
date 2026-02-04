#!/usr/bin/python3
"""
Module qui définit une classe BaseGeometry vide,
servant de classe de base pour la géométrie.
"""


class BaseGeometry:
    """
    Classe de base pour la géométrie.
    Elle contient son aire.
    """
    def area(self):
        """
        Public instance method: def area(self): that raises an Exception
          with the message area() is not implemented
        """
        raise Exception("area() is not implemented")
