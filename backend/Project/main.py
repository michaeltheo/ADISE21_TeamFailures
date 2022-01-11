from fastapi import FastAPI
from . import models
from .database import engine
from .routers import user,Authentication,boards
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI(
)
origins = [
    '*',
    "http://localhost:3000",
]

#when you find a new model added to database
models.Base.metadata.create_all(engine)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Routers
app.include_router(Authentication.router)
app.include_router(user.router)
app.include_router(boards.router)


