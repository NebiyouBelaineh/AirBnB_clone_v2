#!/usr/bin/python3
"""DBStorage engine module"""
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
import os

class DBStorage:
    """DBStorage class"""
    __engine = None
    __session = None
    metadata = MetaData()
    def __init__(self):
        """Initilazier Method"""
        # environment variables:
        hbnb_dev = os.getenv('HBNB_MYSQL_USER')
        hbnb_dev_pwd = os.getenv('HBNB_MYSQL_PWD')
        hbnb_mysql_host = os.getenv('HBNB_MYSQL_HOST')
        hbnb_dev_db = os.getenv('HBNB_MYSQL_DB')
        hbnb_env = os.getenv('HBNB_ENV')
        # hbnb_type_storage = os.getenv('HBNB_TYPE_STORAGE')

        if not DBStorage.__engine:
            self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                        .format(hbnb_dev, hbnb_dev_pwd,
                                                hbnb_mysql_host, hbnb_dev_db
                                                ), pool_pre_ping=True)
        
        
        if hbnb_env == 'test':
            DBStorage.metadata.reflect(bind=self.__engine)
            DBStorage.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """query on the current database session (self.__session) all objects
        depending of the class name (argument cls)"""

        all_dict = {}
        if cls is not None:
            value = self.__session.query(cls)
            key = cls.__name__ + '.' + value.id
            all_dict[key] = value
        else:
            DBStorage.metadata.reflect(bind=self.__engine)
            # metadata.tables is a dictionary-like object where keys are table
            # names and values are Table objects
            all_dict = DBStorage.metadata.tables

        return all_dict

    def new(self, obj):
        """add the object to the current database session (self.__session)"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session (self.__session)"""
        self.__session.commit()

    def delete(self, obj):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)
            

    def reload(self):
        """create all tables in the database """
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review
        # self.__session.close()
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
