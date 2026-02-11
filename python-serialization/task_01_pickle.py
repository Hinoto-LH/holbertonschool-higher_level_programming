#!/usr/bin/python3
"""
Ce module définit la classe CustomObject qui permet de créer
un objet personnalisable pouvant être sérialisé et désérialisé
à l'aide du module pickle.
"""

import pickle


class CustomObject:
    """
    Représente un objet personnalisé contenant un nom,
    un âge et un statut étudiant.

    Cette classe fournit des méthodes pour afficher ses
    informations, ainsi que pour sauvegarder et restaurer
    l'objet à partir d'un fichier en utilisant la sérialisation
    avec pickle.
    """

    def __init__(self, name, age, is_student):
        """
        Initialise une nouvelle instance de CustomObject.

        Args:
            name (str): Le nom de la personne.
            age (int): L'âge de la personne.
            is_student (bool): Indique si la personne est étudiante.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Affiche les informations de l'objet sous un format lisible.

        Cette méthode imprime le nom, l'âge et le statut étudiant
        de l'objet dans un format structuré.
        """
        print("Name: {}\nAge: {}\nis_student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        """
        Sérialise l'objet courant et l'enregistre dans un fichier.

        Args:
            filename (str): Le nom du fichier dans lequel l'objet
            sera sauvegardé en format binaire.

        Cette méthode utilise pickle pour convertir l'objet en
        format binaire et l'écrire dans le fichier spécifié.
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """
        Désérialise un objet CustomObject depuis un fichier.

        Args:
            filename (str): Le nom du fichier contenant
            l'objet sérialisé.

        Returns:
            CustomObject: L'objet restauré depuis le fichier.

        Cette méthode lit le fichier binaire, charge l'objet
        sérialisé avec pickle et retourne l'instance reconstruite.
        """
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return None
