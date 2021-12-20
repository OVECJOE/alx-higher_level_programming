#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
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
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)()
    records = session.query(State).order_by(State.id.asc()).filter(
        State.name.like(r"%a%")
    )
    for record in records:
        print("{}: {}".format(record.id, record.name))
