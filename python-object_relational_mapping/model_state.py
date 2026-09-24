#!/usr/bin/python3
"""Defines the State class, mapped to the MySQL states table."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Represents a US state, linked to the states table."""

    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
