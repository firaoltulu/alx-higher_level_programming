#!/usr/bin/python3
""" This module is the state module."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        uname = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        DATABASE_URL = "mysql://{}:{}@localhost:3306/{}".format(
                uname, password, db_name
                )
        engine = create_engine(DATABASE_URL)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        result = (
                session.query(State).order_by(State.id.asc()).filter(State.name.like("%a%"))
                )
        for res in result:
            print("{}: {}".format(res.id, res.name))
