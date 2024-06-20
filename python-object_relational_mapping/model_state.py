#!/usr/bin/python3
"""script that lists all states from the database"""


from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class State(Base):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    engine = create_engine('mysql+mysqlconnector://username:password@localhost:3306/Saul')

    Base.metadata.create_all(bind=engine)