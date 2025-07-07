#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database using SQLAlchemy ORM and lists all
State objects from the states table that
contain the letter 'a' (case-insensitive)
in their name, ordered by id in ascending order.

Usage:
    ./9-model_state_filter_a.py <username> <password> <database>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to

Functionality:
    - Establishes a connection to a MySQL database using SQLAlchemy ORM.
    - Creates a session to interact with the database.
    - Queries all State objects that have the
            letter 'a' anywhere in their name.
    - Uses LIKE '%a%' pattern matching (case-insensitive).
    - Results are ordered by 'id' in ascending order.
    - Prints each matching state in the format: "id: name"
    - Properly handles database connections and sessions with error handling.

Example usage:
    ./9-model_state_filter_a.py root root hbtn_0e_6_usa

Example output:
    1: California
    2: Arizona
    5: Alabama
    7: Alaska

SQL Query Equivalent:
    SELECT * FROM states WHERE name LIKE '%a%' ORDER BY id ASC;

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
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv, exit
from urllib.parse import quote_plus


def get_state_with_a(mysql_user: str, mysql_passwd: str, mysql_database: str):
    try:
        engine = create_engine(f"mysql+mysqldb://{mysql_user}:{mysql_passwd}@localhost:3306/{mysql_database}")  # noqa: E501
    except SQLAlchemyError as engine_error:
        raise RuntimeError(f"Failed to create engine: {str(engine_error)}")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()  # noqa: E501
        for state in states_with_a:
            print(f"{state.id}: {state.name}")
    except SQLAlchemyError as query_error:
        print(f"Query Failed: {str(query_error)}")
        return
    finally:
        session.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: program username password database")
        exit(1)
    else:
        get_state_with_a(
            quote_plus(argv[1]),
            quote_plus(argv[2]),
            quote_plus(argv[3]))
