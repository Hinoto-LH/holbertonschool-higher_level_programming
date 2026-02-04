#!/usr/bin/python3
"""
Ce module contient une fonction qui vérifie si un objet est
exactement une instance d'une classe donnée.
"""


def is_same_class(obj, a_class):
    """
    Retourne True si l'objet est exactement une instancede la classe spécifiée,
    sinon False.
    """
    return type(obj) is a_class
