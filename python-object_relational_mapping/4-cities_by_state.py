#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database and retrieves all cities
from the 'cities' table, ordered by their id in ascending order.

Usage:
    ./4-cities_by_state.py <username> <password> <database>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to

Functionality:
    - Establishes a connection to a MySQL database using MySQLdb.
    - Executes a SELECT query to fetch all rows from the 'cities' table.
    - Results are ordered by 'id' in ascending order.
    - Prints each row as a tuple in the format: (id, name, state_id)

Example usage:
    ./4-cities_by_state.py root password hbtn_0e_4_usa

Example output:
    (1, 'San Francisco', 'California')
    (2, 'San Jose', 'California')
    (3, 'Los Angeles', 'California')
    (4, 'Fremont', 'California')

Security:
    This script uses safe SQL queries without user input interpolation.

Raises:
    ValueError: If the number of command-line arguments is incorrect.
    MySQLdb.Error: If there's an error connecting to or querying the database.
"""
import MySQLdb
from sys import exit, argv


def get_cities(argv):
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )
    except MySQLdb.Error as conn_error:
        print(f"Connection Failed: {conn_error}")
        return
    cur = db.cursor()
    try:
        cur.execute(
            "SELECT cities.id, cities.name, states.name FROM cities, states\
                WHERE cities.state_id = states.id\
                ORDER BY cities.id ASC"
        )
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as fetch_error:
        try:
            print(
                f"MySQL Error: {fetch_error.args[0]}, \
                {fetch_error.args[1]}"
            )
        except IndexError:
            print(f"MySQL Error: {str(fetch_error)}")
    finally:
        cur.close()
        db.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./program username password database")
        exit(1)
    else:
        get_cities(argv)
