#!/usr/bin/python3
"""This module defines a class to manage the DBstorage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os

class DBStorage:
    """this file manages DBstorage"""

    __engine = None
    __session = None

    def __init__(self):
        """ init method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
            
    def all(self, cls=None):
        """add method"""
        data = {}
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            query = self.__session.query(cls).all()
            for obj in query:
                key = "{}.{}".format(type(cls).__name__, obj.id)
                data[key] = obj
        else:
            list = [User, Place, State, City, Amenity, Review]
            for classes in list:
                query = self.__session.query(classes).all()
                for obj in query:
                    key = "{}.{}".format(type(classes).__name__, obj.id)
                    data[key] = obj
        return data
        
    def new(self, obj):
        """new method"""
        self.__session.add(obj)
    def save(self):
        """save method"""
        self.__session.commit()
    def delete(self, obj=None):
        """delete method"""
        if obj:
            self.__session.delete(obj)
    def reload(self): 
        """reload method"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        session = scoped_session(Session)
        self.__session = session()

    def close(self):
        """calls remove() method"""
        self.__session.close()