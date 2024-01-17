#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from models import storage_type


class Amenity(BaseModel, Base):
    """Defines Amenity class

    Attrinutes:
            name: string - empty string.
            place_amenities: represent a relationship Many-To-Many between
                             the class Place and Amenity
    """
    if storage_type == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""
