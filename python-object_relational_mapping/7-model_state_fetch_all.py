#!/usr/bin/python3
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sys import argv, exit
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus


def list_states_objs(mysql_username: str, mysql_passwd: str, mysql_database: str):
    try:
        engine = create_engine(
            f"mysql+pymysql://{mysql_username}:{mysql_passwd}@localhost:3306/{mysql_database}"
        )
    except SQLAlchemyError as e:
        raise RuntimeError(f"Failed to create engine: {e}")
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        states = session.query(State).order_by(State.id).all()
        for state in states:
            print(f"{state.id}: {state.name}")
    finally:
        session.close()


if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: program username password database")
        exit(1)
    else:
        list_states_objs(quote_plus(argv[1]), quote_plus(argv[2]), quote_plus(argv[3]))
