#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float ,ForeignKey
from sqlalchemy.orm import relationship
from models.user import User
from models.city import City
import models


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    reviews = relationship("Review", cascade="delete", backref="place")

    @property
    def reviews(self):
        """ reviews method """
        dict_reviews = models.storage.all(models.Review)
        list_reviews = []
        for rev in dict_reviews.values():
            if rev.place_id == self.id:
                list_reviews.append(rev)
            return rev
    place_amenity = Table(Base.metadata,
                          Column('place_id', ForeignKey('places.id'), primary_key=True),
                          Column('amenity_id', ForeignKey('amenities.id'), primary_key=True)
                         )
    amenities = relationship("Amenity",
                    secondary=place_amenity, viewonly=False)
    @property
    def amenities(self):
        """getter attribute"""
        dict_amenities = models.storage.all(models.Amenity)
        list_amenities = []
        for obj in dict_amenities:
            if obj.id in amenity_ids:
                list_amenities.append(obj)
        return list_amenities

    @amenities.setter
    def amenitites(self, obj):
        """setter attribute"""
         dict_amenities = models.storage.all(models.Amenity)
        if obj in  dict_amenities:
            amenity_ids.append(obj.id)
