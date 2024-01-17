#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name

    Attributes:
            __tablename__: represents the table name
            name: represents a column containing a string
            state_id: represents a column containing a string
            places: represent a relationship with the class Place
    """
    if models.storage_type == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

        places = relationship('Place', backref='cities',
                              cascade='all, delete-orphan')
    else:
        state_id = ""
        name = ""
