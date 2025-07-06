#!/usr/bin/python3
"""Start link class to table in database"""
import sys
from urllib.parse import quote_plus
from model_state import Base, State

from sqlalchemy import create_engine

if __name__ == "__main__":
    username = quote_plus(sys.argv[1])
    password = quote_plus(sys.argv[2])
    database = quote_plus(sys.argv[3])

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(username, password, database),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)
