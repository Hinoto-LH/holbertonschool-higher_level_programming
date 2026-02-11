#!/usr/bin/python3
"""
Ce module fournit une fonction permettant de convertir
un fichier CSV en fichier JSON.
"""

import csv
import json


def convert_csv_to_json(filename):
    """
    Convertit un fichier CSV en un fichier JSON nommé data.json.

    Args:
        filename (str): Le nom du fichier CSV à convertir.

    Returns:
        bool: True si la conversion est réussie, False en cas d'erreur
        (par exemple si le fichier n'existe pas).
    """
    try:
        # Ouvre le fichier CSV en mode lecture
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            # Convertit chaque ligne du CSV en dictionnaire
            data = list(csv.DictReader(csvfile))

        # Écrit les données converties dans data.json
        with open('data.json', mode='w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True

    except Exception:
        return False
