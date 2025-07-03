#!/usr/bin/python3
''' city model '''
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """
    City class that links to the MySQL 'cities' table.
    Attributes:
        id (int): The city ID, primary key, auto-generated, unique.
        name (str): The name of the city, a string of up to 128 characters.
        state_id (int): The ID of the state that the city belongs
    """
    __tablename__ = 'cities'
    # Defining the columns of the cities table
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    # Establishing relationship between City and State
    state = relationship("State", backref="cities")
