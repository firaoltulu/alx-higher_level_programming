#!/usr/bin/python3
""" This displays all City objects and their State in a database."""
import sys
from sqlalchemy import create_engine, and_, text, tuple_
from sqlalchemy.orm import sessionmaker, relationship
from relationship_state import Base, State
from relationship_city import City

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
        q = session.query(City).join(State).order_by(City.id.asc())
        for city in q.all():
            print("{}: {} -> {}".format(city.id, city.name, city.state.name))
