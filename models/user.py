#!/usr/bin/python3
"""User model for the platform."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """User class for patients, caregivers, and housing providers."""
    __tablename__ = 'users'
    name = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False, unique=True)
    password_hash = Column(String(128), nullable=False)
    role = Column(String(50), nullable=False)  # e.g., 'patient', 'caregiver', 'provider'
    housing_listings = relationship('Housing', backref='user')
    bookings = relationship('Booking', backref='user')
    reviews = relationship('Review', backref='user')