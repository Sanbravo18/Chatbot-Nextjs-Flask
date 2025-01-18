from flask import Blueprint, request, jsonify

users = Blueprint('users', __name__)

@users.route('/users', methods=['GET'])
def get_users():
    # Logic to get users
    users = []  # Replace with actual logic to fetch users
    return jsonify(users)

@users.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Logic to get a single user by ID
    user = {}  # Replace with actual logic to fetch user by ID
    return jsonify(user)

@users.route('/users', methods=['POST'])
def create_user():
    # Logic to create a new user
    data = request.get_json()
    # Replace with actual logic to create a user
    new_user = {"id": 1, "name": data.get("name")}
    return jsonify(new_user), 201

@users.route('/users/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    # Logic to update a user by ID
    data = request.get_json()
    # Replace with actual logic to update a user
    updated_user = {"id": user_id, "name": data.get("name")}
    return jsonify(updated_user)

@users.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Logic to delete a user by ID
    # Replace with actual logic to delete a user
    return jsonify({"message": "User deleted"}), 204