#!/user/bin/pyton3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb

Base = declarative_base()


class State(Base):
    __tbalename__ = 'some_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    db = MySQLdb.connect(
        host="localhost", port=3306,)
