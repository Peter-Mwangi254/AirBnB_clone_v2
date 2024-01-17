#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from models import storage_type


class User(BaseModel, Base):
    """This class defines a user by various attributes

    Attributes:
            email: represents a column containing a string
            password: represents a column containing a string
            firat_name = represents a column containing a string
            last_name = represents a column containing a string
    """
    if storage_type == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
