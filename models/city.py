#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"  # Table name for the City class

    name = Column(String(128), nullable=False)  # Column for city name
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)  # Column for state_id as a foreign key

    # Define the relationship between City and State
    state = relationship("State", back_populates="cities")
