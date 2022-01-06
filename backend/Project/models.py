from sqlalchemy.sql.schema import Column,ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import relationship
from .database import Base
from typing import List
from sqlalchemy.sql.sqltypes import ARRAY

class User(Base):
    __tablename__='Users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    board=relationship('Board',back_populates='creator')


# boards Model
class Board(Base):
    __tablename__='Board'
    id=Column(Integer,primary_key=True,index=True)
    creator_id=Column(Integer,ForeignKey('Users.id'))
    players=Column(ARRAY(String,dimensions=2))
    creator=relationship('User',back_populates='board')
