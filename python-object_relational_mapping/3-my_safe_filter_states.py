#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database and retrieves all states
from the 'states' table where the name exactly matches the provided argument.

Usage:
    ./2-my_filter_states.py <username> <password> <database> <state_name>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to
    state_name  Name of the state to search for (exact match)

Functionality:
    - Establishes a connection to a MySQL database using MySQLdb.
    - Executes a SELECT query to fetch all rows from the 'states' table
      where the name exactly matches the provided argument.
    - Results are ordered by 'id' in ascending order.
    - Prints each matching row as a tuple.

Example usage:
    ./2-my_filter_states.py root password hbtn_0e_0_usa 'Arizona'

Example output:
    (3, 'Arizona')

Raises:
    ValueError: If the number of command-line arguments is incorrect.
    MySQLdb.Error: If there's an error connecting to or querying the database.
"""
import MySQLdb
from sys import exit, argv


def fetch_by_name(argv):
    try:
        db = MySQLdb.connect(
            host='localhost',
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
        # Script that takes in an argument and displays all values
        # in the states table of hbtn_0e_0_usa
        # where name matches the argument.
        cur.execute("SELECT * FROM states\
            WHERE states.name LIKE BINARY %s\
            ORDER BY id ASC", (argv[4],))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as fetch_error:
        try:
            print(f"MySQL Error: \
                {fetch_error.args[0]}, {fetch_error.args[1]}")
        except IndexError:
            print(f"MySQL Error: {str(fetch_error)}")
    finally:
        cur.close()
        db.close()


if __name__ == "__main__":
    if len(argv) != 5:
        print("Usage: ./program username password database keyword")
        exit(1)
    fetch_by_name(argv)
