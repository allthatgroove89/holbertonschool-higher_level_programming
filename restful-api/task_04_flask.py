#!/usr/bin/python3

from flask import Flask
from flask import jsonify


app = Flask(__name__)

user_dict = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}


@app.route("/")
def home():
    return "Welcome to the Flask API!."


@app.route("/data")
def data():
    return jsonify(list(user_dict.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/user_dict/<username>")
def user(username):
    if username in user_dict:
        return jsonify(user_dict[username])
    else:
        return "404 Not Found", 404


if __name__ == "__main__":
    app.run()
