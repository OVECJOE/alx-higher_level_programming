#!/usr/bin/python3
"""
A script that adds the State object "Louisiana" to the database
hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import create_engine
import sys

from model_state import Base, State

if __name__ == "__main__":
    DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
        *sys.argv[1:])
    engine = create_engine(DATABASE_URL)
    session = sessionmaker(bind=engine)()
    session.add(State(name="Louisiana"))
    record = session.query(State).filter(State.name == "Louisiana").first()
    print(record.id if record is not None else "")
