#!/usr/bin/python3



from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
import sys

"""

Create relationship_state file from models_state file. The class attribute
cities must represent a relationship with the class City.
If the State object is deleted, all linked City objects must be
automatically deleted. Also, the reference from a City object
to his State should be named state

"""


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)


 #remember that the engine needs to be passed to a Session object in order to be able to work with the ORM
Session = sessionmaker(bind=engine)
#the base class for defining our classes in order to produce the appropriate Tables
Base = declarative_base()
