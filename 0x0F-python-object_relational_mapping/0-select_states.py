#!/usr/bin/python3

"""
Script that lists all states from the database hbtn_0e_0_usa
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
import sys

if __name__=="__main__":
    Base=declarative_base()
    engine=create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                         format(sys.argv[1], sys.argv[2], sys.argv[3]),pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)


 #define the state model   
class State(Base):
    __tablename__ = 'states'
    id=Column(Integer, primary_key=True, nullable=False) 
    name=Column(String(128), nullable=False)   
#create a session to interact with database

#query all states and print their names
states=session.query(State).order_by(State.id.asc()).all()

for state in states:
    print("({}, '{}')".format(state.id, state.name))

#close the session
session.close()  
