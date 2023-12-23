#!/usr/bin/python3


from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base
from sqlalchemy.orm import relationship 

"""

Create relationship_state file from models_state file. The class attribute
cities must represent a relationship with the class City.
If the State object is deleted, all linked City objects must be
automatically deleted. Also, the reference from a City object
to his State should be named state

"""

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


