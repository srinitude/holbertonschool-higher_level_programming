#!/usr/bin/python3
"""
Creating a State object that inherits from Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    Creating a State object that inherits from Base
    """
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City", back_populates="state")
