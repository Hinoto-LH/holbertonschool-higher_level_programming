#!/usr/bin/python3
def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles d'un objet.

    :param obj: l'objet à inspecter
    :return: une liste contenant les noms des attributs et méthodes
    """

    # dir(obj) renvoie tous les attributs et méthodes accessibles
    # pour l'objet passé en paramètre
    return dir(obj)
