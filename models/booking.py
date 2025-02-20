#!/usr/bin/python3
"""Booking model for the platform."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey

class Booking(BaseModel, Base):
    """Booking class for housing reservations."""
    __tablename__ = 'bookings'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    housing_id = Column(String(60), ForeignKey('housing_listings.id'), nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    status = Column(String(50), nullable=False)  # e.g., 'pending', 'confirmed', 'canceled'