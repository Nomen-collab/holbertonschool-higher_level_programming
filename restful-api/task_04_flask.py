#!/usr/bin/python3

from flask import Flask, jsonify, request
import json


app = Flask(__name__)

# In-memory storage for users
users = {}


# Route for the root URL
@app.route('/')
def home():
    return "Welcome to the Flask API!"


# Route to serve JSON data with usernames
@app.route('/data')
def data():
    return jsonify(list(users.keys()))


# Route for status
@app.route('/status')
def status():
    return "OK"


# Route to get a specific user's data
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return app.response_class(
            json.dumps(user, indent=4, sort_keys=False),
            content_type='application/json')
    else:
        return jsonify({"error": "User not found"}), 404


# Route to add a new user
@app.route('/add_user', methods=['POST'])
def add_user():
    # Parse the incoming JSON data
    user_data = request.get_json()

    # Ensure 'username' is included in the data
    if not user_data.get('username'):
        return jsonify({"error": "Username is required"}), 400

    # Add user to the dictionary
    users[user_data['username']] = user_data

    # Return a confirmation message with the user data
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


# Run the Flask development server
if __name__ == "__main__":
    app.run()
