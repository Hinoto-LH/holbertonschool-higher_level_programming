#!/usr/bin/python3
"""
Ce module contient une fonction qui vérifie si un objet est une instance
d'une classe héritée d'une classe donnée.
"""


def inherits_from(obj, a_class):
    """
    Retourne True si l'objet est une instance d'une classe qui hérite
    directement ou indirectement de la classe spécifiée, sinon False.

    Args:
        obj: l'objet à vérifier
        a_class: la classe de référence

    Returns:
        bool: True ou False selon le cas
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
    # type(obj) is not a class /exclut les instances direct"""
