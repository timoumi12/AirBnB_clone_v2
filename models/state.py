#!/usr/bin/python3
""" State Module for HBNB project """
import shlex
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    if os.getenv('HBNB_TYPE_STORAGE') != "db":
        @property
        def cities(self):
            var = models.storage.all()
            _list = []
            result = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    _list.append(var[key])
            for elem in _list:
                if (elem.state_id == self.id):
                    result.append(elem)
            return (result)
