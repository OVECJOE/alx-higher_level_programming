#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine("mysql://{}:{}@localhost:3306/{}"
                           .format(*sys.argv[1:]))
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    record = session.query(State).first()
    if record is not None:
        print("{}: {}".format(record.id, record.name))
    else:
        print("Nothing")
