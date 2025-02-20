#!/usr/bin/python3
"""Place model for the platform."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Place(BaseModel, Base):
    """Place class for housing listings."""
    __tablename__ = 'places'
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    price_per_night = Column(Float, nullable=False)
    amenities = relationship('Amenity', secondary='place_amenity', backref='places')
    bookings = relationship('Booking', backref='place')
    reviews = relationship('Review', backref='place')