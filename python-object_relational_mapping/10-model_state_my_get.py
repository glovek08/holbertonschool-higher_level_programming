#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database using SQLAlchemy ORM and searches for
a specific State object by name. If found, it prints the state's ID.
If not found, it prints "Not found".

Usage:
    ./10-model_state_my_get.py <username> <password> <database> <state_name>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to
    state_name  Name of the state to search for (exact match)

Functionality:
    - Establishes a connection to a MySQL database using SQLAlchemy ORM.
    - Creates a session to interact with the database.
    - Queries for a State object with the exact name provided.
    - Uses filter_by() for exact name matching.
    - Uses first() to get only the first matching result.
    - Prints the state's ID if found, or "Not found" if no match exists.
    - Properly handles database connections and sessions with error handling.

Example usage:
    ./10-model_state_my_get.py root root hbtn_0e_6_usa California

Example output (if found):
    1

Example output (if not found):
    Not found

SQL Query Equivalent:
    SELECT * FROM states WHERE name = 'state_name' LIMIT 1;

Security:
    - Uses URL encoding for database credentials to handle special characters
    - Uses SQLAlchemy ORM with filter_by() to prevent SQL injection attacks
    - Properly closes database sessions even if errors occur

Error Handling:
    - Handles engine creation failures with RuntimeError
    - Handles query failures with graceful error messages
    - Uses try-finally blocks to ensure proper session cleanup

Implementation Notes:
    - Uses filter_by(name=state_name) for exact string matching
    - Uses first() instead of all() since we only need one result
    - Only prints the ID number, not the full "id: name" format

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
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from urllib.parse import quote_plus


def get_state_by_name(mysql_username: str,
                      mysql_passwd: str,
                      mysql_database: str,
                      state_name: str):
    try:
        engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_passwd}@localhost:3306/{mysql_database}")  # noqa: E501
    except SQLAlchemyError as engine_error:
        raise RuntimeError(f"Failed to create engine: {str(engine_error)}")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        state_by_name = session.query(State).filter_by(name=state_name).first()
        if state_by_name is None:
            print("Not found")
        else:
            print(f"{state_by_name.id}")
    except SQLAlchemyError as query_error:
        print(f"Query Failed: {str(query_error)}")
        return
    finally:
        session.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: program username password database state_name_to_search")
        exit(1)
    else:
        get_state_by_name(
            quote_plus(argv[1]),
            quote_plus(argv[2]),
            quote_plus(argv[3]),
            quote_plus(argv[4]))
