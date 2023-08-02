#!/usr/bin/python3
"""Create class inherits from Base """

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class City(Base):
    """
    State class that represents a state table in MySQL
    """
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True,)
    name = Column(String(128), nullable=False)
    state_id = Column(String,  ForeignKey("state_id"), nullable=False)

    