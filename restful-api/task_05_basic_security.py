from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required,
    get_jwt_identity, get_jwt,
    # Importez les décorateurs pour la gestion des erreurs JWT
    # Ces gestionnaires d'erreurs garantissent un statut 401 pour toutes les erreurs d'authentification JWT
    unauthorized_loader, invalid_token_loader, expired_token_loader,
    revoked_token_loader, needs_fresh_token_loader
)
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# Initialisation de l'application Flask
app = Flask(__name__)

# Configuration de la clé secrète pour JWT
# En production, cette clé devrait être stockée de manière sécurisée (par ex. variables d'environnement)
app.config["JWT_SECRET_KEY"] = "super-secret-key-please-change-me" # TRÈS IMPORTANT : Utilisez une clé forte et unique !
jwt = JWTManager(app)

# Initialisation de l'authentification de base
auth = HTTPBasicAuth()

# Base de données d'utilisateurs en mémoire
# Les mots de passe sont hachés pour la sécurité
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("admin_password"), "role": "admin"}
}

# --- Gestionnaires d'erreurs personnalisés pour JWT ---
# Ces fonctions sont appelées automatiquement par Flask-JWT-Extended
# en cas d'erreur de token et renvoient une réponse 401 cohérente.

@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({"error": "Signature verification failed"}), 401

@jwt.expired_token_loader
def expired_token_response(callback):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def revoked_token_response(callback):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def needs_fresh_token_response(callback):
    return jsonify({"error": "Fresh token required"}), 401

# --- Fonctions de vérification pour Basic Auth ---

@auth.verify_password
def verify_password(username, password):
    """
    Vérifie les identifiants pour l'authentification HTTP Basic.
    """
    if username in users and \
       check_password_hash(users[username]["password"], password):
        return username  # Retourne le nom d'utilisateur si les identifiants sont valides
    return None # Retourne None si les identifiants sont invalides

# --- Routes de l'API ---

@app.route('/')
def home():
    """Route racine."""
    return "Welcome to the API!"

@app.route('/basic-protected', methods=['GET'])
@auth.login_required # Cette route nécessite une authentification HTTP Basic
def basic_protected():
    """
    Route protégée par l'authentification HTTP Basic.
    Accès uniquement si les identifiants Basic Auth sont valides.
    """
    return "Basic Auth: Access Granted"

@app.route('/login', methods=['POST'])
def login():
    """
    Route de connexion pour obtenir un token JWT.
    Accepte le nom d'utilisateur et le mot de passe en JSON.
    """
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    # Vérifie les identifiants
    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Crée un token d'accès JWT
    # L'identité est le nom d'utilisateur.
    # additional_claims permet d'inclure des données supplémentaires dans le token (comme le rôle de l'utilisateur).
    access_token = create_access_token(
        identity=username,
        expires_delta=datetime.timedelta(hours=1), # Le token expire après 1 heure
        additional_claims={"role": user["role"]}
    )
    return jsonify(access_token=access_token)

@app.route('/jwt-protected', methods=['GET'])
@jwt_required() # Cette route nécessite un token JWT valide
def jwt_protected():
    """
    Route protégée par l'authentification JWT.
    Accès uniquement si un token JWT valide est fourni.
    """
    # Récupère l'identité de l'utilisateur à partir du token JWT
    current_user = get_jwt_identity()
    return f"JWT Auth: Access Granted for user {current_user}"

@app.route('/admin-only', methods=['GET'])
@jwt_required() # Cette route nécessite un token JWT valide
def admin_only():
    """
    Route protégée par JWT avec contrôle d'accès basé sur les rôles.
    Accès uniquement si l'utilisateur a le rôle 'admin'.
    """
    claims = get_jwt() # Récupère toutes les revendications (claims) du token JWT
    if claims and claims.get("role") == "admin":
        return "Admin Access: Granted"
    else:
        # Si le rôle n'est pas 'admin', renvoie une erreur 403 Forbidden
        return jsonify({"error": "Admin access required"}), 403

# Lance le serveur Flask en mode développement
if __name__ == "__main__":
    # Désactivez debug=True en production !
    app.run(debug=True, port=5000)
