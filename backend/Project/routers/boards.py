from fastapi import APIRouter,Depends
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import func, mode
from sqlalchemy.sql.expression import func
from .. import schemas, database,models
from ..repository import boards
from typing import List

router=APIRouter(
    prefix='/board',
    tags=['Board']
)

@router.post('/')
def create_board(request:schemas.Boards,db:Session=Depends(database.get_db)):
    return boards.create_board(request,db)

@router.get('/',response_model=List[schemas.Boards])
def get_boards(db:Session=Depends(database.get_db)):
    return boards.get_boards(db)

@router.get('/{id}',response_model=schemas.Boards)
def get_board(id:int,db:Session=Depends(database.get_db)):
    return boards.get_board(id,db)