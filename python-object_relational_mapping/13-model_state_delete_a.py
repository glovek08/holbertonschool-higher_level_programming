#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database using SQLAlchemy ORM and deletes all
State objects from the states table whose names contain the letter 'a'.

Usage:
    ./13-model_state_delete_a.py <username> <password> <database>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to

Functionality:
    - Establishes a connection to a MySQL database using SQLAlchemy ORM.
    - Creates a session to interact with the database.
    - Selects all State objects whose name contains the letter 'a'.
    - Deletes all such State objects from the database.
    - Commits the transaction to save the changes.
    - Handles database errors and rolls back the transaction if needed.
    - Properly closes the session after execution.

Example usage:
    ./13-model_state_delete_a.py root root hbtn_0e_6_usa

Security:
    - Uses URL encoding for database credentials to handle special characters
    - Uses SQLAlchemy ORM to prevent SQL injection attacks
    - Properly closes database sessions even if errors occur

Error Handling:
    - Handles SQLAlchemyError exceptions and rolls back on error
    - Uses try-finally blocks to ensure proper session cleanup

Dependencies:
    - SQLAlchemy (ORM framework)
    - MySQLdb (MySQL database driver)
    - model_state module (containing State class)
    - urllib.parse (for URL encoding credentials)

Raises:
    SQLAlchemyError: If a database error occurs (handled gracefully)
    SystemExit: If incorrect number of command-line arguments provided
"""

from sqlalchemy import create_engine, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from model_state import State
from urllib.parse import quote_plus as qp
from sys import exit, argv


def delete_all_with_a(
    mysql_username: str,
    mysql_passwd: str,
    mysql_database: str
):
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_passwd}@localhost:3306/{mysql_database}")  # noqa: E501
    with Session(engine) as session:
        try:
            stmt = select(State).where(State.name.contains('a'))
            states_to_delete = session.scalars(stmt).all()
            for state in states_to_delete:
                session.delete(state)
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            print(f"An error occurred: {e}")
            return


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./program username password database")
        exit(1)
    else:
        delete_all_with_a(
            qp(argv[1]),
            qp(argv[2]),
            qp(argv[3])
        )
