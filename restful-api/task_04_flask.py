#!/usr/bin/python3
"""
This module contains a Flask API with several routes.
"""

from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Home route. Returns a welcome message.
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def get_usernames():
    """
    Returns a list of usernames stored in the 'users' dictionary.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Returns a status message.
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Returns the data for a given user, or a 404 error if the user is not found.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'User Not Found'}), 404


@app.route("/add_user", methods=['POST'])
def add_user():
    new_user = request.json
    username = new_user.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username == users:
        return ({"error": "User already exists"}), 400
    users[username] = new_user
    return jsonify({"message": "User added", "user": new_user}), 201


if __name__ == "__main__":
    app.run()
