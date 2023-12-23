#!/usr/bin/python3

"""
Start link class to table in database
checks if documented
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database
from base import Base, Session, engine
from relationship_state import State
from relationship_city import City


if __name__ == "__main__":
    

    Base.metadata.create_all(bind=engine, checkfirst=True)
    


    session = Session()
    
    state = State("Utah")
    session.add(City("san fransico", state))
    session.commit()
    session.close()

