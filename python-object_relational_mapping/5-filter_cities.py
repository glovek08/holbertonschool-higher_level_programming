#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database and retrieves all cities
that belong to a specific state. The cities are displayed as a
comma-separated list, ordered by their appearance in the database.

Usage:
    ./5-filter_cities.py <username> <password> <database> <state_name>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to
    state_name  Name of the state to filter cities by

Functionality:
    - Establishes a connection to a MySQL database using MySQLdb.
    - Executes a SELECT query with INNER JOIN to fetch city names
      from the 'cities' table that belong to the specified state.
    - Uses parameterized queries to prevent SQL injection attacks.
    - Displays the results as a comma-separated list of city names.

Example usage:
    ./5-filter_cities.py root password hbtn_0e_4_usa California

Example output:
    San Francisco, San Jose, Los Angeles, Fremont, Livermore

Database Schema:
    cities table: id, name, state_id
    states table: id, name

Security:
    This script uses parameterized queries to prevent SQL injection attacks.

Raises:
    ValueError: If the number of command-line arguments is incorrect.
    MySQLdb.Error: If there's an error connecting to or querying the database.
"""

from sys import argv, exit
import MySQLdb


def get_state_by_name(argv):
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3]
        )
    except MySQLdb.Error as conn_error:
        print(f"MySQL Error: {conn_error}")
        return
    cur = db.cursor()
    try:
        cur.execute("SELECT cities.name FROM cities \
            INNER JOIN states \
            ON states.id = cities.state_id and states.name = %s\
            ORDER BY cities.id ASC", (argv[4],))
        cities = []
        for row in cur.fetchall():
            cities.append(row[0])
        print(", ".join(cities))
    except MySQLdb.Error as fetch_error:
        try:
            print(f"MySQL Error: {fetch_error.args[0]}, \
                {fetch_error.args[1]}")
        except IndexError:
            print(f"MySQL Error: {str(fetch_error)}")
    finally:
        cur.close()
        db.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: program username password database state_name")
        exit(1)
    else:
        get_state_by_name(argv)
