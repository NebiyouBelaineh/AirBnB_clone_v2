#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import relationship
import os
from datetime import datetime


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    
    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))
    updated_at = Column(DateTime, nullable=False, default=(datetime.utcnow()))

    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', cascade='all, delete-orphan', backref='state')
    else:
        @property
        def cities(self):
            from models.city import City
            """
            Getter attribute that returns a list of City instances
            with state_id equals to the provided state_id.
            """
            from models import storage

            cities_list = []
            for city_instance in storage.all(City).values():
                if city_instance.state_id == self.id:
                    cities_list.append(city_instance)
            return cities_list
