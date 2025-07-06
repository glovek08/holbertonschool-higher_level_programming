#!/usr/bin/python3
"""
This script connects to a MySQL database using SQLAlchemy and retrieves all rows from the 'states' table,
ordered by the 'id' column. The database connection parameters (username, password, database name) are
provided as command-line arguments.

Usage:
    ./script.py <username> <password> <database>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to

Functionality:
    - Establishes a connection to a MySQL database using SQLAlchemy.
    - Reflects the 'states' table from the database schema.
    - Executes a SELECT query to fetch all rows from the 'states' table, ordered by 'id'.
    - Prints each row as a tuple.

Raises:
    ValueError: If the number of command-line arguments is incorrect.
"""

from sys import argv
import MySQLdb
from sqlalchemy import create_engine, MetaData, Table, select
from sqlalchemy.engine.url import URL

if __name__ == "__main__":
    if len(argv) != 4:
        raise ValueError("Usage: ./script.py username password database")
    else:
        url = URL.create(
            drivername="mysql+mysqldb",
            username=argv[1],
            password=argv[2],
            host="localhost",
            port=3306,
            database=argv[3],
        )
        engine = create_engine(url)
        metadata = MetaData()
        states = Table("states", metadata, autoload_with=engine)

        with engine.connect() as conn:
            stmt = select(states).order_by(states.c.id)
            result = conn.execute(stmt)
            for row in result:
                print(row)
