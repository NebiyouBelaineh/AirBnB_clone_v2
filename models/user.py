#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
import os
from datetime import datetime


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        places = relationship(
            'Place', cascade='all, delete-orphan', backref='user')
        reviews = relationship(
            'Review', cascade='all, delete-orphan', backref='user')
