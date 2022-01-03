from fastapi import FastAPI,Depends
from . import schemas,models
from .database import engine,SessionLocal
from sqlalchemy.orm import Session
from passlib.context import CryptContext

app=FastAPI()

#when you find a new model added to database
models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#hashing
pwd_cxt=CryptContext(schemes=["bcrypt"], deprecated="auto")


@app.post('/user')
def create_user(request:schemas.User,db:Session=Depends(get_db)):
  #hash password
  hashedPassword=pwd_cxt.hash(request.password)
  new_user=models.User(
      name=request.name,
      email=request.email,
      password=hashedPassword
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user
   