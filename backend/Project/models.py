from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from typing import List
from sqlalchemy.sql.sqltypes import ARRAY, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects import postgresql
import uuid


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    board = relationship("Board", back_populates="creator")


# boards Model
class Board(Base):
    __tablename__ = "Board"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    creator_id = Column(Integer, ForeignKey("Users.id"))
    players = Column(postgresql.ARRAY(String))
    board = Column(postgresql.ARRAY(String))
    isFull = Column(Boolean)
    creator = relationship("User", back_populates="board")
