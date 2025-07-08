#!/usr/bin/python3
# fmt: off
"""
This module defines the City class for SQLAlchemy ORM.
Contains the class definition of a City.
"""
from model_state import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String


class City(Base):
    """
    City class that inherits from Base and links to the MySQL table cities.

    Attributes:
        id: Column of auto-generated, unique integer, primary key, not null
        name: Column of string with maximum 128 characters, not null
        state_id: Foreign key, the id of the state to
        which the city belongs to.
    """
    __tablename__ = "cities"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        nullable=False,
        autoincrement=True)
    name: Mapped[str] = mapped_column(String(128), nullable=False)
    state_id: Mapped[int] = mapped_column(
        ForeignKey("states.id"),
        nullable=False)

    def __repr__(self) -> str:
        return f"<City(id={self.id},\
            name={self.name!r}, state_id={self.state_id})>"
