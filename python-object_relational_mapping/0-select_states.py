#!/usr/bin/python3

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
