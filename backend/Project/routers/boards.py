from fastapi import APIRouter,Depends
from sqlalchemy.orm.session import Session
from .. import schemas, database,oauth2
from ..repository import boards
from typing import List

router=APIRouter(
    prefix='/board',
    tags=['Board']
)

@router.post('/')
def create_board(request:schemas.Boards,db:Session=Depends(database.get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
    return boards.create_board(request,db)

@router.get('/',response_model=List[schemas.Boards])
def get_boards(db:Session=Depends(database.get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
    return boards.get_boards(db)

@router.get('/{id}',response_model=schemas.Boards)
def get_board(id:int,db:Session=Depends(database.get_db),get_current_user:schemas.User=Depends(oauth2.get_current_user)):
    return boards.get_board(id,db)