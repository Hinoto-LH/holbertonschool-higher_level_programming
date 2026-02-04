#!/usr/bin/python3
"""
Module qui définit une classe BaseGeometry vide,
servant de classe de base pour la géométrie.
"""


class BaseGeometry:
    """
    Classe de base pour la géométrie.

    Fournit les méthodes area() et integer_validator()
    pour être utilisées ou surchargées par les classes filles.
    """
    def area(self):
        """
        Public instance method.

        Lève une exception indiquant que la méthode n'est pas implémentée.

        Raises:
            Exception: toujours avec le message "area() is not implemented"
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Vérifie que 'value' est un entier strictement positif.

        Args:
            name (str): nom de l'attribut pour les messages d'erreur
            value (int): valeur à valider

        Raises:
            TypeError: si value n'est pas un entier
            ValueError: si value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
