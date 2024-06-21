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

    engine = create_engine(f"mysql+mysqldb: //
                           {username}: {password}@localhost: 3306/{database}")
    Session = sessionmaker(bind=engine)
    session = Session
    # Query the State object with id=2, retreive the object
    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        state_to_update.name = "New Mexico"  # Change the name attribute
        session.commit()  # Commit the change to de DB
