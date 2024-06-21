#!/usr/bin/python3
"""script that deletes all State objects with a name
    containing the letter a from the database"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query that joins State and City by City.id
    results = session.query(
        State, City).join(
            City, State.id == City.state_id).order_by(City.id).all()

    for state, city in results:
        print(f"{state.name}: ({city.id}) {city.name}")
    session.close()
