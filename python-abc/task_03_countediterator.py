#!/usr/bin/python3
"""
Module qui définit la classe CountedIterator.

Cette classe permet d'itérer sur un iterable tout en comptant
le nombre d'éléments retournés.
"""


class CountedIterator:
    """
    Itérateur qui compte le nombre d'éléments itérés.
    """

    def __init__(self, iterable):
        """
        Initialise le compteur et l'itérateur.

        Args:
            iterable: objet itérable
        """
        self.count = 0
        self.it = iter(iterable)

    def __next__(self):
        """
        Retourne l'élément suivant de l'itérateur
        et incrémente le compteur.

        Returns:
            élément suivant de l'itérable
        """
        self.count += 1
        return next(self.it)

    def __iter__(self):
        """
        Retourne l'itérateur lui-même.

        Returns:
            self
        """
        return self

    def get_count(self):
        """
        Retourne le nombre d'éléments déjà itérés.

        Returns:
            int: nombre d'éléments itérés
        """
        return self.count
