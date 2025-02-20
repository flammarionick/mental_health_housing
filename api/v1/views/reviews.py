#!/usr/bin/python3
"""API endpoints for reviews."""
from flask import jsonify, request, abort
from models import storage
from models.review import Review
from api.v1.views.app_views import app_views

@app_views.route('/reviews', methods=['GET'], strict_slashes=False)
def get_reviews():
    """Get all reviews."""
    reviews = storage.all(Review).values()
    return jsonify([review.to_dict() for review in reviews])

@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review_by_id(review_id):
    """Get a specific review by ID."""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())

@app_views.route('/reviews', methods=['POST'], strict_slashes=False)
def create_review():
    """Create a new review."""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    if 'housing_id' not in data:
        abort(400, description="Missing housing_id")
    if 'rating' not in data:
        abort(400, description="Missing rating")
    if 'text' not in data:
        abort(400, description="Missing text")
    review = Review(**data)
    review.save()
    return jsonify(review.to_dict()), 201

@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    """Update a review by ID."""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(review.to_dict())

@app_views.route('/reviews/<review_id>', methods=['DELETE'], strict_slashes=False)
def delete_review(review_id):
    """Delete a review by ID."""
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    review.delete()
    return jsonify({}), 200