#!/usr/bin/python3
"""
This module defines the State class for SQLAlchemy ORM.
Contains the class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class that inherits from Base and links to the MySQL table states.

    Attributes:
        id: Column of auto-generated, unique integer, primary key, not null
        name: Column of string with maximum 128 characters, not null
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
