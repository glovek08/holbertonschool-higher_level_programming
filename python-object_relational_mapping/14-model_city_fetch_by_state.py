#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database using SQLAlchemy ORM and fetches all
cities along with their corresponding state names. The results are displayed
in the format "state_name: (city_id) city_name", ordered by city id.

Usage:
    ./14-model_city_fetch_by_state.py <username> <password> <database>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to

Functionality:
    - Establishes a connection to a MySQL database using SQLAlchemy ORM.
    - Creates a session to interact with the database.
    - Performs a JOIN query between State and City tables.
    - Selects state name, city id, and city name from the joined tables.
    - Orders results by city id in ascending order.
    - Displays each result in the format: "state_name: (city_id) city_name"
    - Handles database errors and rolls back the transaction if needed.

Example usage:
    ./14-model_city_fetch_by_state.py root root hbtn_0e_14_usa

Example output:
    California: (1) San Francisco
    California: (2) San Jose
    California: (3) Los Angeles
    Texas: (4) Dallas
    Texas: (5) Houston

SQL Query Equivalent:
    SELECT states.name, cities.id, cities.name
    FROM states
    JOIN cities ON states.id = cities.state_id
    ORDER BY cities.id ASC;

Security:
    - Uses URL encoding for database credentials to handle special characters
    - Uses SQLAlchemy ORM to prevent SQL injection attacks
    - Properly closes database sessions even if errors occur

Error Handling:
    - Handles SQLAlchemyError exceptions and rolls back on error
    - Uses session context manager for automatic cleanup

Dependencies:
    - SQLAlchemy (ORM framework)
    - MySQLdb (MySQL database driver)
    - model_state module (containing State class)
    - model_city module (containing City class)
    - urllib.parse (for URL encoding credentials)

Raises:
    SQLAlchemyError: If a database error occurs (handled gracefully)
    SystemExit: If incorrect number of command-line arguments provided
"""

from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from urllib.parse import quote_plus
from sys import argv, exit
from model_state import State
from model_city import City


def get_cities(
        mysql_username: str,
        mysql_passwd: str,
        mysql_database: str):
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_passwd}@localhost:3306/{mysql_database}")  # noqa: E501
    with Session(engine) as session:
        try:
            stmt = (
                select(State.name, City.id, City.name)
                .join(City, State.id == City.state_id)
                .order_by(City.id)
            )
            results = session.execute(stmt).all()
            for state_name, city_id, city_name in results:
                print(f"{state_name}: ({city_id}) {city_name}")
        except SQLAlchemyError as query_error:
            session.rollback()
            print(f"An error occurred: {query_error}")
            return


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./program username password database")
        exit(1)
    else:
        get_cities(
            quote_plus(argv[1]),
            quote_plus(argv[2]),
            quote_plus(argv[3]))
