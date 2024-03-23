#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
import os
from datetime import datetime


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"

    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship(
            'Place', cascade='all, delete-orphan', backref='cities')
