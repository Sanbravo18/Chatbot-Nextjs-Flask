from flask import Blueprint, request, jsonify
from werkzeug.exceptions import HTTPException
import asyncio

users = Blueprint('users', __name__)


@users.route('/users', methods=['GET'])
async def get_users():
    try:
        await asyncio.sleep(1)
        users_list = []  # Replace with actual logic to fetch users
        return jsonify(users_list)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise Exception(f"Chats request failed: {str(e)}")

@users.route('/users/<string:user_id>', methods=['GET'])
async def get_user(user_id):
    try:
        await asyncio.sleep(1)  # Simulate async operation
        user = {}  # Replace with actual logic to fetch user by ID
        return jsonify(user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise Exception(f"Chats request failed: {str(e)}")

@users.route('/users', methods=['POST'])
async def create_user():
    try:
        data =  {"name":"pedrito"}   #await request.get_json()
        # Replace with actual logic to create a user
        new_user = {"id": 1, "name": data.get("name")}
        return jsonify(new_user), 201
    except HTTPException as e:
        raise e
    except Exception as e:
        raise Exception(f"Chats request failed: {str(e)}")

@users.route('/users/<string:user_id>', methods=['PATCH'])
async def update_user(user_id):
    try:
        data =  {"id": "1","name":"juanito"}  # await request.get_json()
        # Replace with actual logic to update a user
        updated_user = {"id": user_id, "name": data.get("name")}
        return jsonify(updated_user)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise Exception(f"Chats request failed: {str(e)}")

@users.route('/users/<string:user_id>', methods=['DELETE'])
async def delete_user(user_id):
    try:
        await asyncio.sleep(1)  # Simulate async operation
        # Replace with actual logic to delete a user
        return jsonify({"message": "User deleted"}), 204
    except HTTPException as e:
        raise e
    except Exception as e:
        raise Exception(f"Chats request failed: {str(e)}")
