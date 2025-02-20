#!/usr/bin/python3
"""Amenity model for the platform."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Amenity class for housing listings."""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    housing = relationship('Housing', secondary='housing_amenity', backref='amenities')