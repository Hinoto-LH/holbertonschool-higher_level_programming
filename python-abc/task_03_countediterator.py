#!/usr/bin/python3
"""
Module qui définit la classe CountedIterator.

Cette classe étend un itérateur Python standard
et garde une trace du nombre d'éléments itérés.
"""


class CountedIterator:
    """
    Itérateur qui compte combien d'éléments ont été parcourus.
    """

    def __init__(self, iterable):
        """
        Initialise l'itérateur et le compteur.

        Args:
            iterable: un objet itérable
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        Retourne l'élément suivant et incrémente le compteur.

        Returns:
            élément suivant de l'itérable

        Raises:
            StopIteration: lorsque l'itérable est épuisé
        """
        value = next(self.iterator)
        # Lève StopIteration automatiquement si terminé
        self.count += 1
        return value

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
