#!/usr/bin/python3
"""Script that prints the first State object from the database"""


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).first()
    if states:
        for state in states:
            print(state.name)
    else:
        print("No states found in database")

    session.close()
