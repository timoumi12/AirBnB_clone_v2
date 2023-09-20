#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float ,ForeignKey, Table
from sqlalchemy.orm import relationship
from models.user import User
from models.city import City
import models
place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    amenities = relationship("Amenity", secondary='place_amenity',
                             back_populates="place_amenities", viewonly=False)
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
    @property
    def amenities(self):
        """getter attribute"""
        dict_amenities = models.storage.all(models.Amenity)
        list_amenities = []
        for obj in dict_amenities:
            if obj.id in Place.amenity_ids:
                list_amenities.append(obj)
        return list_amenities

    @amenities.setter
    def amenitites(self, obj):
        """setter attribute"""
        dict_amenities = models.storage.all(models.Amenity)
        if obj in  dict_amenities:
            Place.amenity_ids.append(obj.id)
