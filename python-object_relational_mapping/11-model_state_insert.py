#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database using SQLAlchemy ORM and inserts a new
State object with the name 'Louisiana' into the states table. After insertion,
it prints the new state's id.

Usage:
    ./11-model_state_insert.py <username> <password> <database>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to

Functionality:
    - Establishes a connection to a MySQL database using SQLAlchemy ORM.
    - Creates a session to interact with the database.
    - Inserts a new State object with the name 'Louisiana'.
    - Commits the transaction and prints the new state's id.
    - Handles database connection and query errors gracefully.
    - Properly closes the session after execution.

Example usage:
    ./11-model_state_insert.py root root hbtn_0e_6_usa

Example output:
    6

Security:
    - Uses URL encoding for database credentials to handle special characters
    - Uses SQLAlchemy ORM to prevent SQL injection attacks
    - Properly closes database sessions even if errors occur

Error Handling:
    - Handles engine creation failures with RuntimeError
    - Handles query failures with graceful error messages
    - Uses try-finally blocks to ensure proper session cleanup

Dependencies:
    - SQLAlchemy (ORM framework)
    - MySQLdb (MySQL database driver)
    - model_state module (containing State class and Base)
    - urllib.parse (for URL encoding credentials)

Raises:
    RuntimeError: If database engine creation fails
    SQLAlchemyError: If database query fails (handled gracefully)
    SystemExit: If incorrect number of command-line arguments provided
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from model_state import Base, State
from urllib.parse import quote_plus
from sys import exit, argv


def insert_louisiana(
        mysql_username: str,
        mysql_passwd: str,
        mysql_database: str):
    try:
        engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_passwd}@localhost/{mysql_database}")  # noqa: E501
    except SQLAlchemyError as engine_error:
        raise RuntimeError(f"Engine creation error: {engine_error}")
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name="Louisiana")
    try:
        session.add(new_state)
        session.commit()
        print(new_state.id)
    except SQLAlchemyError as query_error:
        print(f"Couldn't add resource: {query_error}")
        return
    finally:
        session.close()


if __name__ == "__main__":
    if (len(argv)) != 4:
        print("Usage: program username password database")
        exit(1)
    else:
        insert_louisiana(
            quote_plus(argv[1]),
            quote_plus(argv[2]),
            quote_plus(argv[3]))
