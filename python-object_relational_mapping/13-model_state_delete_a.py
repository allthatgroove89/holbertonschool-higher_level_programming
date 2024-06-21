#!/usr/bin/python3
"""script that changes the name of a State object from the database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_delete = session.query(State).filter(State.name).first()
    if state_to_delete:
        state_to_delete.name = "a"
        session.commit()
