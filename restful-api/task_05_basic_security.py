#!/usr/bin/python3
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()


users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]["password"], password):
        return username


@app.route("/")
def home():
    return "Home!"


@app.route("/basic-protected")
@auth.login_required
def index():
    return "Basic Auth: Access Granted"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)


# app = Flask(__name__)
# auth = HTTPTokenAuth(scheme="Bearer")

# tokens = {
#     'secret-token-1': 'john',
#     'secret-token-2': 'susan',
# }

# @auth.verify_token
# def verify_token(token):
#     if token in tokens:
#         return tokens[token]

# @app.route('/')
# @auth.login_required
# def index():
#     return "Hello, {}!".format(auth.current_user())

# if __name__ == '__main__':
#     app.run()
