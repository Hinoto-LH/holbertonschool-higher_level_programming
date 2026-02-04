#!/usr/bin/python3
"""
Ce module définit une classe MyList qui hérite de la classe list
et permet d’afficher la liste triée sans la modifier.
"""


class MyList(list):
    """
    Classe qui hérite de list et ajoute une méthode
    pour afficher la liste triée.
    """
    def print_sorted(self):
        """
        Affiche la liste triée par ordre croissant
        sans modifier la liste originale.
        """
        print(sorted(self))
