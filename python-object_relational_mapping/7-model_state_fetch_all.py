#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database using SQLAlchemy ORM and lists all
State objects from the states table, ordered by their id in ascending order.

Usage:
    ./7-model_state_fetch_all.py <username> <password> <database>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to

Functionality:
    - Establishes a connection to a MySQL database using SQLAlchemy ORM.
    - Creates a session to interact with the database.
    - Queries all State objects from the states table ordered by id.
    - Prints each state in the format: "id: name"
    - Properly handles database connections and sessions.

Example usage:
    ./7-model_state_fetch_all.py root password hbtn_0e_6_usa

Example output:
    1: California
    2: Arizona
    3: Texas
    4: New York
    5: Nevada

Database Requirements:
    - MySQL server running on localhost:3306
    - Database with 'states' table matching the State model
    - Valid user credentials with read access

Security:
    - Uses URL encoding for database credentials to handle special characters
    - Uses SQLAlchemy ORM to prevent SQL injection attacks
    - Properly closes database sessions

Raises:
    RuntimeError: If database engine creation fails
    SQLAlchemyError: If database connection or query fails
    SystemExit: If incorrect number of command-line arguments provided

Dependencies:
    - SQLAlchemy
    - PyMySQL (as the MySQL driver)
    - model_state module (containing State class and Base)
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sys import argv, exit
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


def list_states_objs(mysql_username: str,
                     mysql_passwd: str,
                     mysql_database: str):
    try:
        engine = create_engine(
            f"mysql+mysqldb://{mysql_username}:{mysql_passwd}@localhost:3306/{mysql_database}"
        )
    except SQLAlchemyError as e:
        raise RuntimeError(f"Failed to create engine: {e}")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: program username password database")
        exit(1)
    else:
        list_states_objs(
            quote_plus(argv[1]),
            quote_plus(argv[2]),
            quote_plus(argv[3]))
