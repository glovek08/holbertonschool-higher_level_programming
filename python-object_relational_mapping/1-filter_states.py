#!/usr/bin/python3
# fmt: off
"""
This script connects to a MySQL database and retrieves all states
whose names start with 'N' (uppercase N) from the 'states' table,
ordered by the 'id' column in ascending order.

Usage:
    ./1-filter_states.py <username> <password> <database>

Arguments:
    username    MySQL database username
    password    MySQL database password
    database    Name of the MySQL database to connect to

Functionality:
    - Establishes a connection to a MySQL database using MySQLdb.
    - Executes a SELECT query to fetch all rows from the 'states' table
      where the name starts with 'N', ordered by 'id' in ascending order.
    - Prints each row as a tuple in the format: (id, 'state_name')

Example output:
    (4, 'New York')
    (5, 'Nevada')

Raises:
    ValueError: If the number of command-line arguments is incorrect.
    MySQLdb.Error: If there's an error connecting to or querying the database.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    if len(argv) != 4:
        raise ValueError(
            "Usage: ./1-filter_states.py username password database"
        )
    else:
        try:
            db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=argv[1],
                passwd=argv[2],
                db=argv[3]
            )
        except MySQLdb.Error as conn_error:
            print(f"Connection failed: {conn_error}")
        cur = db.cursor()
        try:
            query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
            cur.execute(query)
            rows = cur.fetchall()
        except MySQLdb.Error as fetch_error:
            try:
                print(
                    "MySQL Error [{}]: {}".format(
                        fetch_error.args[0], fetch_error.args[1]
                    )
                )
            except IndexError:
                print("MySQL Error: {}".format(str(fetch_error)))
        for row in rows:
            print(row)
        cur.close()
        db.close()
