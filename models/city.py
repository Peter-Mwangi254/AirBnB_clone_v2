#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from models.base_model import BaseModel, Base
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name

    Attributes:
            __tablename__: represents the table name
            name: represents a column containing a string
            state_id: represents a column containing a string
    """
    if models.storage_type == 'db':
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    else:
        state_id = ""
        name = ""
