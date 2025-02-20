#!/usr/bin/python3
"""Housing model for the platform."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Housing(BaseModel, Base):
    """Housing class for listings."""
    __tablename__ = 'housing_listings'
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    price_per_night = Column(Float, nullable=False)
    amenities = relationship('Amenity', secondary='housing_amenity', backref='housing')
    bookings = relationship('Booking', backref='housing')
    reviews = relationship('Review', backref='housing')