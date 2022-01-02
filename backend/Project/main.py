from fastapi import FastAPI
from .schemas import User

app=FastAPI()


@app.post('/user')
def create_user(request:User):
    return request
   