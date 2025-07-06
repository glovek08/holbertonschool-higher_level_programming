#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database using SQLAlchemy ORM and prints the
first State object from the states table, ordered by id.

Usage:
    ./8-model_state_fetch_first.py <username> <password> <database>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to

Functionality:
    - Establishes a connection to a MySQL database using SQLAlchemy ORM.
    - Creates a session to interact with the database.
    - Queries the first State object from the states table (ordered by id).
    - Prints the state in the format: "id: name"
        or "Nothing" if no states exist.
    - Properly handles database connections and sessions with error handling.

Example usage:
    ./8-model_state_fetch_first.py root root test_8

Example output:
    1: California

    OR if no states exist:
    Nothing

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


from sys import argv, exit
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


def get_first_state(mysql_user: str,
                    mysql_passwd: str,
                    mysql_db: str):
    try:
        # Use var to store the url cause pycode's 80 line limit's been a bitch
        url = f"mysql+mysqldb://{mysql_user}:\
            {mysql_passwd}@localhost:3306/{mysql_db}"
        engine = create_engine(url)
    except SQLAlchemyError as engine_error:
        raise RuntimeError(f"Failed to create engine: {engine_error}")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        first_state = session.query(State).first()
        if first_state is None:
            print("Nothing")
        else:
            print(f"{first_state.id}: {first_state.name}")
    except SQLAlchemyError as query_error:
        print(f"Query failed: {query_error}")
        return
    finally:
        session.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: program username password database")
        exit(1)
    get_first_state(quote_plus(argv[1]),
                    quote_plus(argv[2]),
                    quote_plus(argv[3]))
