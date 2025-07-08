#!/usr/bin/python3
"""
This module defines the State class for SQLAlchemy ORM.
Contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Any


class Base(DeclarativeBase):
    pass


class State(Base):
    """
    State class that inherits from Base and links to the MySQL table states.

    Attributes:
        id: Column of auto-generated, unique integer, primary key, not null
        name: Column of string with maximum 128 characters, not null
    """

    __tablename__ = "states"
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True, nullable=False
    )
    name: Mapped[str] = mapped_column(String(128), nullable=False)

    def __repr__(self) -> str:
        return f"<State(id={self.id}, name='{self.name!r}')>"
