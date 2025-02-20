#!/usr/bin/python3
"""API endpoints for users."""
from flask import jsonify, request, abort
from models import storage
from models.user import User
from api.v1.views.app_views import app_views

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """Get all users."""
    users = storage.all(User).values()
    return jsonify([user.to_dict() for user in users])

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Get a specific user by ID."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Create a new user."""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'email' not in data:
        abort(400, description="Missing email")
    if 'password_hash' not in data:
        abort(400, description="Missing password")
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update a user by ID."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a user by ID."""
    user = storage.get(User, user_id)
    if not user:
        abort(404)
    user.delete()
    return jsonify({}), 200