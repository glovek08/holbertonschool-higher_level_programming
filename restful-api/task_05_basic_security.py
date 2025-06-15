#!/usr/bin/python3
from flask import Flask, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "sofi": generate_password_hash("sofiIsCuteAF"),
    "fede": generate_password_hash("fedePlaysGuitar"),
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required
def index():
    return "Hello, {}!".format(auth.current_user())

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)


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