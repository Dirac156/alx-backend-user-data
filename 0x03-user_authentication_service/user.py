#!/usr/bin/env python3
""" User base module """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    """ The main class for users """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=false)
    hashed_password = Column(String(250), nullable=false)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
