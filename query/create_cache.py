import os
import sys
from sqlalchemy import Column, Integer, String, Date, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import pickle

Base = declarative_base()

class cache(Base):
    __tablename__ = 'cache_2019'

    # Notice that each column is also a normal Python instance attribute.
    company_jobtitle = Column(String(128), primary_key = True)
    company = Column(String(64), nullable = False)
    jobtitle = Column(String(64), nullable= False, index = True)
    result = Column(DECIMAL(15, 3))
    frequency = Column(Integer(15)) 

# Create an engine that stores data on Google Cloud
with open('credentials.pkl', 'rb') as f:
    cred = pickle.load(f)

engine = create_engine('mysql+pymysql://' + cred['user'] + ':' + cred['password'] + '@127.0.0.1/' + cred['database2'])
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)
