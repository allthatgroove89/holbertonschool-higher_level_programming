#!/usr/bin/python3
"""script that prints the State object with the name passed as argument"""


import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import create_engine


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_to_search = sys.argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        state = session.query(State).filter
        (State.name == state_name_to_search).one()
        print(state.id)
    except NoResultFound:
        print("Not found")
