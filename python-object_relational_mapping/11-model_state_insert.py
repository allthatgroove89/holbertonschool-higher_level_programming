#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database"""


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # Create engine
    engine = create_engine("mysql+mysqldb://{}, {}@localhost:3306/{}"
                           .format(username, password, database))
    # Create session and bind engine to the sessionmaker
    Session = sessionmaker(bind=engine)
    session = Session()
    # Create a new State object to the session
    louisiana = State(name="Louisiana")
    # Add the created State to the session
    session.add(louisiana)
    # Commiting session to the db to save new State
    session.commit()
    # Print the Id of the new State
    print(louisiana.id)
    # Closing session
    session.close()
