#!/usr/bin/python3
from flask import Flask, jsonify, request

users = {
    "jane": {
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles",
    },
    "maicon": {
        "name": "Maicon",
        "age": 23,
        "city": "San Francisco",
    },
    "fede": {
        "name": "Federico",
        "age": 29,
        "city": "Montevideo"
    }
}

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def return_usernames():
    username = list(users.keys())
    return jsonify(username=username)


@app.route("/status")
def return_status():
    return "OK"


@app.route("/users/<username>")
def return_user_data(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run()
