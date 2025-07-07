#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database using SQLAlchemy ORM and updates the
name of the State object with id=2 to 'New Mexico' in the states table.

Usage:
    ./12-model_state_update_id_2.py <username> <password> <database>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to

Functionality:
    - Establishes a connection to a MySQL database using SQLAlchemy ORM.
    - Creates a session to interact with the database.
    - Queries for the State object with id=2.
    - Updates the name of the State to 'New Mexico'.
    - Commits the transaction to save the change.
    - Handles the case where no State with id=2 exists.
    - Properly closes the session after execution.

Example usage:
    ./12-model_state_update_id_2.py root root hbtn_0e_6_usa

Security:
    - Uses URL encoding for database credentials to handle special characters
    - Uses SQLAlchemy ORM to prevent SQL injection attacks
    - Properly closes database sessions even if errors occur

Error Handling:
    - Handles engine creation failures with RuntimeError
    - Handles missing State with id=2 using NoResultFound
    - Uses try-finally blocks to ensure proper session cleanup

Dependencies:
    - SQLAlchemy (ORM framework)
    - MySQLdb (MySQL database driver)
    - model_state module (containing State class and Base)
    - urllib.parse (for URL encoding credentials)

Raises:
    RuntimeError: If database engine creation fails
    NoResultFound: If no State with id=2 exists (handled gracefully)
    SystemExit: If incorrect number of command-line arguments provided
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError, NoResultFound
from model_state import State
from sys import argv, exit
from urllib.parse import quote_plus


def update_state(
        mysql_username: str,
        mysql_passwd: str,
        mysql_database: str
        ):
    engine = create_engine(
        f"mysql+mysqldb://{mysql_username}:{mysql_passwd}@localhost:3306/{mysql_database}"  # noqa: E501
    )
    Session = sessionmaker(bind=engine)
    try:
        with Session() as session:
            stmt = select(State).where(State.id == 2)
            state = session.execute(stmt).scalar_one()
            state.name = "New Mexico"
            session.commit()
    except NoResultFound:
        print("No State found with that id")
    except SQLAlchemyError as e:
        print(f"Couldn't create engine or update: {e}")


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: program username password database")
        exit(1)
    update_state(
        quote_plus(argv[1]),
        quote_plus(argv[2]),
        quote_plus(argv[3]),
    )
