from lib2to3.pgen2.token import OP
from typing import List
from fastapi.param_functions import Body
from pydantic import BaseModel
from typing import Optional
from uuid import UUID

from sqlalchemy.sql.sqltypes import Boolean


class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    id: int
    name: str
    email: str
    # password:str

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


class Boards(BaseModel):
    id: Optional[UUID]
    creator_id: Optional[int]
    creator: Optional[ShowUser]
    players: Optional[List]
    board: Optional[List]
    active_player: Optional[str]
    isFull: Optional[bool]
    status: Optional[str]

    class Config:
        orm_mode = True
