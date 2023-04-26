#!/usr/bin/python3
"""
This script retrieves all states from a MySQL database and prints them to the terminal.

Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb
import sys

if __name__=="__main__":
    Base=declarative_base()
    engine=create_engine("mysql+mysqldb://{}:{}@localhost/{}".
                         format(sys.argv[1], sys.argv[2], sys.argv[3]))
 """define the state model"""  
class State(Base):
    __tablename__ = 'states'
    id=Column(Integer, primary_key=True, nullable=False) 
    name=Column(String(128), nullable=False)   
"""create a session to interact with database"""
Session=sessionmaker(bind=engine)
session=Session()
"""query all states and print their names"""
states=session.query(State).order_by(State.id.asc()).all()

for state in states:
    print("({}, '{}')".format(state.id, state.name))

"""close the session"""
session.close()   
