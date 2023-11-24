#!/usr/bin/python3

""" This is a state model """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()
""" This represents the base class """


class State(Base):
    """This class will display a row"""

    __tablename__ = "states"
    id = Column(
            Integer, autoincrement=True, unique=True, nullable=False, primary_key=True
            )
    name = Column(String(length=128), nullable=False)
