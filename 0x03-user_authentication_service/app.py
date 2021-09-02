#!/usr/bin/env python
""" App """
import flask
from auth import Auth


app = flask.Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def hello() -> str:
    """ return welcome message """
    msg = {"message": "Bienvenue"}
    return flask.jsonify(msg)


@app.route('/users', methods=['POST'])
def register() -> str:
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


@app.route('/sessions', methods=['POST'])
def login() -> str:
    """ Login the user """
    form_data = flask.request.form

    if "email" not in form_data:
        return flask.jsonify({"message": "email required"}), 400
    elif "password" not in form_data:
        return flask.jsonify({"message": "password required"}), 400
    else:

        email = flask.request.form.get("email")
        pswd = flask.request.form.get("password")

        if AUTH.valid_login(email, pswd) is False:
            flask.abort(401)
        else:
            session_id = AUTH.create_session(email)
            response = flask.jsonify({
                "email": email,
                "message": "logged in"
                })
            response.set_cookie('session_id', session_id)

            return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
