#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import os
import uuid
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
# from models import storage


Base = declarative_base()
class BaseModel:
    """A base class for all hbnb models"""

    id = Column(String(60), unique=True, nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        from models import storage
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            if os.getenv('HBNB_TYPE_STORAGE') != 'db':
                storage.new(self)

        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            # for every key-value pair,
            # instance attribute is created from dictionary
            # Should be tested
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.__dict__.update(kwargs)
            
    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)  # moved from def __init__
        storage.save()


    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        key_to_remove = '_sa_instance_state'
        if key_to_remove in dictionary:
            del dictionary[key_to_remove]
        return dictionary

    def delete(self):
        """Delets the current instance from storage"""
        from models import storage
        storage.delete(self)
