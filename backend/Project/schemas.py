from pydantic import BaseModel
from sqlalchemy.sql.functions import user

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