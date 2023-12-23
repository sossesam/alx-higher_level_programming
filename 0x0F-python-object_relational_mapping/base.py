from sqlalchemy import create_engine 
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker
import sys

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)


 #remember that the engine needs to be passed to a Session object in order to be able to work with the ORM
Session = sessionmaker(bind=engine)
#the base class for defining our classes in order to produce the appropriate Tables
Base = declarative_base()
