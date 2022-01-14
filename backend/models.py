from typing import List
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.dialects import postgresql
from sqlalchemy.dialects.postgresql import UUID
import uuid

from sqlalchemy.sql.sqltypes import Boolean
from .database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    boards = relationship("Boards", back_populates="creator")


class Boards(Base):
    __tablename__ = "Boards"
    id = Column(UUID(as_uuid=True), primary_key=True)
    creator_id = Column(Integer, ForeignKey("Users.id"))
    players = Column(postgresql.ARRAY(String))
    board = Column(postgresql.ARRAY(String))
    active_player = Column(String)
    isFull = Column(Boolean)

    creator = relationship("User", back_populates="boards")
