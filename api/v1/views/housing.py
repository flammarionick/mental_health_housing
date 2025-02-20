#!/usr/bin/python3
"""API endpoints for housing listings."""
from flask import jsonify, request, abort
from models import storage
from models.housing import Housing
from api.v1.views.app_views import app_views

@app_views.route('/housing', methods=['GET'], strict_slashes=False)
def get_housing():
    """Get all housing listings."""
    housing = storage.all(Housing).values()
    return jsonify([h.to_dict() for h in housing])

@app_views.route('/housing/<housing_id>', methods=['GET'], strict_slashes=False)
def get_housing_by_id(housing_id):
    """Get a specific housing listing by ID."""
    housing = storage.get(Housing, housing_id)
    if not housing:
        abort(404)
    return jsonify(housing.to_dict())

@app_views.route('/housing', methods=['POST'], strict_slashes=False)
def create_housing():
    """Create a new housing listing."""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'name' not in data:
        abort(400, description="Missing name")
    if 'description' not in data:
        abort(400, description="Missing description")
    if 'city_id' not in data:
        abort(400, description="Missing city_id")
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    if 'price_per_night' not in data:
        abort(400, description="Missing price_per_night")
    housing = Housing(**data)
    housing.save()
    return jsonify(housing.to_dict()), 201

@app_views.route('/housing/<housing_id>', methods=['PUT'], strict_slashes=False)
def update_housing(housing_id):
    """Update a housing listing by ID."""
    housing = storage.get(Housing, housing_id)
    if not housing:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(housing, key, value)
    housing.save()
    return jsonify(housing.to_dict())

@app_views.route('/housing/<housing_id>', methods=['DELETE'], strict_slashes=False)
def delete_housing(housing_id):
    """Delete a housing listing by ID."""
    housing = storage.get(Housing, housing_id)
    if not housing:
        abort(404)
    housing.delete()
    return jsonify({}), 200