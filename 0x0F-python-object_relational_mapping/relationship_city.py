#!/usr/bin/python3
"""
Creating a City object that inherits from Base
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """
    Creating a City object that inherits from Base
    """
    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                autoincrement=True,
                nullable=False)
    name = Column(String(128),
                  nullable=False)
    state_id = Column(Integer,
                      ForeignKey("states.id"),
                      nullable=False)
    state = relationship("State", back_populates="cities")
