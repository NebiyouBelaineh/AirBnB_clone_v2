#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
import os
from datetime import datetime


class Amenity(BaseModel, Base):
    """Class Amenity"""
    __tablename__ = "amenities"

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship(
            'Place', secondary='place_amenity',
            back_populates="amenities",
            viewonly=False)
