#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage_type
from models.city import City


class State(BaseModel, Base):
    """State class inherits from BaseModel and Base
    """
    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            '''returns the list of City instances with state_id
                equals the current State.id
                FileStorage relationship between State and City
            '''
            from models import storage
            cities_list = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
