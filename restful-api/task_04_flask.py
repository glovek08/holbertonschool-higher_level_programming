#!/usr/bin/python3
from flask import Flask, jsonify

# users = {"jane": {"name": "Jane", "age": 28, "city": "Los Angeles"}}

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def return_usernames():
    username = list(users.keys())[0]
    return jsonify(username=username)

@app.route("/status")
def return_status():
    return "OK"

if __name__ == "__main__":
    app.run()