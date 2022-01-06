from pydantic import BaseModel
from sqlalchemy.sql.functions import user
from typing import Optional,List
from uuid import UUID

class User(BaseModel):
    name:str
    email:str
    password:str


class ShowUser(BaseModel):
    name:str
    email:str

    class Config():
        orm_mode=True

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

class Boards(BaseModel):
    id:Optional[UUID]
    creator_id:int
    creator:Optional[ShowUser]
    players:Optional[ShowUser]
    board:Optional[List[str]]
    class Config():
        orm_mode=True
