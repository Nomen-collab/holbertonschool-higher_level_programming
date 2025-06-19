from flask import Flask, jsonify, request

# Initialise l'application Flask
app = Flask(__name__)

# Base de données en mémoire pour stocker les utilisateurs
# C'est un dictionnaire où la clé est le nom d'utilisateur (username)
# et la valeur est un dictionnaire contenant toutes les informations de l'utilisateur.
# IMPORTANT : Laissez ce dictionnaire vide pour la soumission.
users = {}

@app.route('/')
def home():
    """
    Route racine de l'API.
    Retourne un message de bienvenue.
    """
    return "Welcome to the Flask API!"

@app.route('/data')
def get_users_data():
    """
    Endpoint /data.
    Retourne une liste de tous les noms d'utilisateurs enregistrés dans l'API.
    """
    # jsonify convertit la liste Python en une réponse JSON avec le bon Content-Type.
    return jsonify(list(users.keys()))

@app.route('/status')
def get_status():
    """
    Endpoint /status.
    Retourne simplement le statut "OK" pour indiquer que l'API est fonctionnelle.
    """
    return "OK"

@app.route('/users/<username>')
def get_user(username):
    """
    Endpoint dynamique /users/<username>.
    Retourne les informations complètes d'un utilisateur spécifique.
    Si l'utilisateur n'est pas trouvé, retourne une erreur 404.
    """
    user = users.get(username) # Tente de récupérer l'utilisateur par son nom d'utilisateur
    if user:
        return jsonify(user) # Si l'utilisateur existe, renvoie ses données JSON
    else:
        # Si l'utilisateur n'est pas trouvé, renvoie un message d'erreur avec un statut 404
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Endpoint /add_user.
    Accepte les requêtes POST pour ajouter un nouvel utilisateur.
    Attend des données JSON dans le corps de la requête.
    Gère les erreurs (nom d'utilisateur manquant, utilisateur déjà existant).
    """
    # Récupère les données JSON envoyées dans le corps de la requête.
    # Flask analyse automatiquement le JSON si le Content-Type est application/json.
    new_user = request.get_json()

    # Vérifie si les données sont présentes et si le 'username' est fourni.
    if not new_user or 'username' not in new_user:
        # Renvoie une erreur 400 Bad Request si le username est manquant.
        return jsonify({"error": "Username is required"}), 400

    username = new_user['username']

    # Vérifie si l'utilisateur existe déjà pour éviter les doublons.
    if username in users:
        # Renvoie une erreur 409 Conflict si l'utilisateur existe déjà.
        return jsonify({"error": "User already exists"}), 409

    # Ajoute le nouvel utilisateur au dictionnaire en mémoire.
    users[username] = new_user

    # Renvoie un message de confirmation avec les données de l'utilisateur ajouté
    # et un code de statut 201 Created pour indiquer une ressource créée.
    return jsonify({"message": "User added", "user": new_user}), 201

# Bloc pour lancer le serveur Flask en mode développement.
# Le mode debug=True permet le rechargement automatique du serveur
# lors des modifications du code et fournit des messages d'erreur détaillés.
if __name__ == "__main__":
    app.run(debug=True)
