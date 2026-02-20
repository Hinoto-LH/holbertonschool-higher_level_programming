#!/usr/bin/python3
"""
Module Flask pour une API de gestion d'utilisateurs.
Ce module fournit des endpoints pour gérer des profils utilisateurs en mémoire.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de données en mémoire (vide au départ pour le checker)
users = {}


@app.route("/")
def home():
    """
    Affiche un message de bienvenue.
    Returns:
        str: Message de bienvenue.
    """
    return "Welcome to the Flask API!"


@app.route("/status")
def status():
    """
    Retourne le statut de l'API.
    Returns:
        str: Le message 'OK'.
    """
    return "OK"


@app.route("/data")
def get_usernames():
    """
    Récupère la liste de tous les noms d'utilisateurs.
    Returns:
        JSON: Liste des clés du dictionnaire users.
    """
    return jsonify(list(users.keys()))


@app.route("/users/<username>")
def get_user(username):
    """
    Récupère l'objet utilisateur complet via son pseudo.
    Args:
        username (str): Pseudo à rechercher.
    Returns:
        JSON: Profil complet ou message d'erreur 404.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Ajoute un nouvel utilisateur à partir d'un corps JSON.
    Returns:
        JSON: Confirmation de création ou erreur (400, 409).
    """
    # Vérification si le JSON est valide
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Vérification du champ username
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Vérification si l'utilisateur existe déjà
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Ajout de l'utilisateur
    users[username] = data
    return jsonify({
        "message": "User added successfully",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
