#!/usr/bin/python3

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from base import Base, Session, engine
from relationship_state import State
from relationship_city import City

"""

Create relationship_state file from models_state file. The class attribute
cities must represent a relationship with the class City.
If the State object is deleted, all linked City objects must be
automatically deleted. Also, the reference from a City object
to his State should be named state

"""

if __name__ == "__main__":
    

    Base.metadata.create_all(bind=engine, checkfirst=True)
    


    session = Session()
    
    state = State("Utah")
    session.add(City("san fransico", state))
    session.commit()
    session.close()

