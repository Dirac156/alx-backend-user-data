#!/usr/bin/env python3
""" App """
import flask
from auth import Auth


app = flask.Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def hello_world() -> str:
    """ return welcome message """
    msg = {"message": "Bienvenue"}
    return flask.jsonify(msg)


@app.route('/users', methods=['POST'])
def register_user() -> str:
    """ Add a new user to the db """
    try:
        email = flask.request.form['email']
        password = flask.request.form['password']
    except KeyError:
        flask.abort(400)

    try:
        AUTH.register_user(email, password)
    except ValueError:
        return flask.jsonify({"message": "email already registered"}), 400

    msg = {"email": email, "message": "user created"}
    return flask.jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
