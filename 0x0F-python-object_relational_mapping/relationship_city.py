#!/usr/bin/python3

"""
Creation of a new file, relationship_city for the
City class from models_city
Start link class to table in database
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base
from sqlalchemy.orm import relationship 


class City(Base):
    """
    this is a class kdkd
    """

    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True,
                primary_key=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state  = relationship('State', backref='city') 


    def __init__(self, name, state):
        self.name = name
        self.state = state


