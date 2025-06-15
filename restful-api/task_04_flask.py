#!/usr/bin/python3
from flask import Flask, jsonify, request

# users = {
#     "jane": {
#         "name": "Jane",
#         "age": 28,
#         "city": "Los Angeles",
#     },
#     "maicon": {
#         "name": "Maicon",
#         "age": 23,
#         "city": "San Francisco",
#     },
#     "fede": {
#         "name": "Federico",
#         "age": 29,
#         "city": "Montevideo"
#     }
# }

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def return_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)


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


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = data
    return jsonify({
        "message": "User added",
        "user": data
    }), 201


if __name__ == "__main__":
    app.run()
