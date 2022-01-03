from fastapi import FastAPI,Depends
from . import schemas,models,hashing
from .database import engine,SessionLocal
from sqlalchemy.orm import Session


app=FastAPI()

#when you find a new model added to database
models.Base.metadata.create_all(engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()




@app.post('/user')
def create_user(request:schemas.User,db:Session=Depends(get_db)):
  new_user=models.User(
      name=request.name,
      email=request.email,
      password=hashing.Hash.bcrypt(request.password)
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user
   