from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user


app=FastAPI()

#when you find a new model added to database
models.Base.metadata.create_all(engine)

#Routers
app.include_router(user.router)


