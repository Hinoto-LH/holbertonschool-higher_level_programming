#!/usr/bin/python3
from flask import Flask, jsonify, request
"""
Docstring pour home
"""

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "bob": {"username": "bob", "name": "Bob Jones", "age": 32, "city": "London"}
}


@app.route("/")
def home():
    """
    Affiche un message de bienvenue sur la racine de l'API.

    Returns:
        str: Message de bienvenue textuel.
    """
    return ("Welcome to the Flask API!")


# Route /data (Liste de tous les noms d'utilisateurs)
@app.route("/data")
def get_all_users():
    """
    Récupère la liste de tous les noms d'utilisateurs.
    ---
    responses:
      200:
        description: Une liste JSON contenant uniquement les pseudos (clés).
    """
    # On extrait juste les clés (les noms d'utilisateurs)
    return jsonify(list(users.keys()))


# Route dynamique /users/<username>
@app.route("/users/<username>")
def get_user_profile(username):
    """
    Récupère l'objet complet d'un utilisateur via son pseudo.
    ---
    parameters:
      - name: username
        in: path
        type: string
        required: true
        description: Le pseudo de l'utilisateur à rechercher.
    responses:
      200:
        description: L'objet utilisateur complet.
      404:
        description: Erreur si l'utilisateur n'existe pas.
    """
    # On cherche l'utilisateur dans notre dictionnaire\
    #  (en minuscules pour être flexible)
    user = users.get(username.lower())

    if user:
        return jsonify(user)
    else:
        # On retourne un message d'erreur et le code HTTP 404
        return jsonify({"error": "User not found"}), 404


# NOUVELLE ROUTE : Ajouter un utilisateur
@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Ajoute un nouvel utilisateur à la base de données.
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: User
          required:
            - username
          properties:
            username:
              type: string
            name:
              type: string
            age:
              type: integer
            city:
              type: string
    responses:
      201:
        description: Utilisateur ajouté avec succès.
      400:
        description: JSON invalide ou champ 'username' manquant.
      409:
        description: Conflit si le pseudo existe déjà.
    """
    # 1. Vérifier si le corps est un JSON valide
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # 2. Vérifier si le champ 'username' est présent
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # 3. Vérifier si l'utilisateur existe déjà (conflit)
    username_key = username.lower()
    if username_key in users:
        return jsonify({"error": "Username already exists"}), 409

    # 4. Ajouter l'utilisateur et confirmer
    users[username_key] = data
    return jsonify({"message": "User added successfully", "user": data}), 201


if __name__ == "__main__":
    app.run(port=5000, debug=True)
