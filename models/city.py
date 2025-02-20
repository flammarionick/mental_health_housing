#!/usr/bin/python3
"""City model for the platform."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """City class for housing locations."""
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)
    country = Column(String(128), nullable=False, default="UK")
    housing_listings = relationship('Housing', backref='city')