from fastapi import FastAPI,Depends
from .schemas import User
from .database import engine,SessionLocal
from sqlalchemy.orm import Session

app=FastAPI()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post('/user')
def create_user(request:User):
    return request
   