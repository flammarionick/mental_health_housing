#!/usr/bin/python3
"""Review model for the platform."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

class Review(BaseModel, Base):
    """Review class for housing feedback."""
    __tablename__ = 'reviews'
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    housing_id = Column(String(60), ForeignKey('housing_listings.id'), nullable=False)
    rating = Column(Integer, nullable=False)  # e.g., 1-5 stars
    text = Column(String(1024), nullable=False)