from flask import Blueprint, request
from database import get_db
import bcrypt
import jwt
from datetime import datetime, timedelta
import os

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    json_data = request.get_json()
    # json_data has password and username only
    username = json_data["username"]
    password = json_data["password"]

    db = get_db()
    cursor = db.cursor
    try:
        salt = cursor.execute("SELECT salt FROM users WHERE username = %s", username)
        input = salt + password
        real_password = cursor.execute("SELECT hashed_password FROM users WHERE username = %s", username)
        if (bcrypt.hashpw(input, salt) == real_password):
            return jwt.encode({"username": username}, "loggedIn", algorithm="HS256")
    except Exception as e:
        return jsonify({"error": "User doesn't exist"}), 404
    
    # TODO: Implement login logic
    
    return jsonify({"message": "Login successful"}), 200


@auth_bp.route("/register", methods=["POST"])
def register():
    json_data = request.get_json()
    # json_data has password and username only
    username = json_data["username"]
    password = json_data["password"]

    db = get_db()
    cursor = db.cursor
    new_salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(passowrd, new_salt)
    # INSERT INTO users value (username, password) VALUES (?, ?)
    # TODO: Implement register logic
    try:
        cursor.execute("INSERT INTO users (username, hashed_password, salt) VALUES (%s, %s, %s)", (username, hashed_password, new_salt))
    except Exception as e:
        return jsonify({"error": "User already exists!"}), 409

    return jsonify({"message": "Login successful"}), 200
