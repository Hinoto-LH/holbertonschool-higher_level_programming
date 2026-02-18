#!/usr/bin/python3
"""
Module pour interagir avec l'API JSONPlaceholder.

Ce module fournit des fonctions permettant de récupérer des articles (posts),
d'afficher leurs titres et de les sauvegarder dans un fichier CSV local.
"""
import csv
import requests


def fetch_and_print_posts():
    """
    Récupère les articles et affiche le code de statut et les titres.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        response = requests.get(url)
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            posts = response.json()
            for post in posts:
                print(post.get('title'))
        else:
            print("Échec de la récupération des données.")

    except Exception as e:
        print(f"Une erreur est survenue : {e}")


def fetch_and_save_posts():
    """
    Récupère les articles et les sauvegarde dans 'posts.csv'.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            posts = response.json()

            # Structuration des données demandée pour le projet
            data_to_save = []
            for post in posts:
                data_to_save.append({
                    'id': post.get('id'),
                    'title': post.get('title'),
                    'body': post.get('body')
                })

            # Écriture dans le fichier CSV
            with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
                fieldnames = ['id', 'title', 'body']
                writer = csv.DictWriter(f, fieldnames=fieldnames)

                writer.writeheader()
                writer.writerows(data_to_save)

            print("Données sauvegardées avec succès dans posts.csv")
        else:
            print(f"Erreur HTTP : {response.status_code}")

    except Exception as e:
        print(f"Une erreur est survenue lors de la sauvegarde : {e}")


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
