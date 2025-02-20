#!/usr/bin/python3
"""API endpoints for bookings."""
from flask import jsonify, request, abort
from models import storage
from models.booking import Booking
from api.v1.views.app_views import app_views

@app_views.route('/bookings', methods=['GET'], strict_slashes=False)
def get_bookings():
    """Get all bookings."""
    bookings = storage.all(Booking).values()
    return jsonify([booking.to_dict() for booking in bookings])

@app_views.route('/bookings/<booking_id>', methods=['GET'], strict_slashes=False)
def get_booking_by_id(booking_id):
    """Get a specific booking by ID."""
    booking = storage.get(Booking, booking_id)
    if not booking:
        abort(404)
    return jsonify(booking.to_dict())

@app_views.route('/bookings', methods=['POST'], strict_slashes=False)
def create_booking():
    """Create a new booking."""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if 'user_id' not in data:
        abort(400, description="Missing user_id")
    if 'housing_id' not in data:
        abort(400, description="Missing housing_id")
    if 'start_date' not in data:
        abort(400, description="Missing start_date")
    if 'end_date' not in data:
        abort(400, description="Missing end_date")
    booking = Booking(**data)
    booking.save()
    return jsonify(booking.to_dict()), 201

@app_views.route('/bookings/<booking_id>', methods=['PUT'], strict_slashes=False)
def update_booking(booking_id):
    """Update a booking by ID."""
    booking = storage.get(Booking, booking_id)
    if not booking:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(booking, key, value)
    booking.save()
    return jsonify(booking.to_dict())

@app_views.route('/bookings/<booking_id>', methods=['DELETE'], strict_slashes=False)
def delete_booking(booking_id):
    """Delete a booking by ID."""
    booking = storage.get(Booking, booking_id)
    if not booking:
        abort(404)
    booking.delete()
    return jsonify({}), 200