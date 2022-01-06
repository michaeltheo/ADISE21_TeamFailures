from pydantic import BaseModel
from sqlalchemy.sql.functions import user
from typing import Optional

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
    id:Optional[int]
    creator_id:int
    creator:Optional[ShowUser]
    class Config():
        orm_mode=True