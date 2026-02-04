#!/usr/bin/python3
"""
Ce module contient une fonction qui vérifie si un objet est
une instance d'une classe donnée ou d'une classe qui en hérite.
"""


def is_kind_of_class(obj, a_class):
    """
    Retourne True si l'objet est une instance de la classe spécifiée
    ou d'une classe qui en hérite, sinon False.

    Args:
        obj: l'objet à vérifier
        a_class: la classe de référence

    Returns:
        bool: True ou False selon le cas
    """
    return isinstance(obj, a_class)
