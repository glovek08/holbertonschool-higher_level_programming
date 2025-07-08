#!/usr/bin/python3
# fmt: off

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
