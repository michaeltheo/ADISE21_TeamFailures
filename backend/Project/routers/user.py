from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm.session import Session
from .. import schemas,models,hashing,database
from sqlalchemy.orm import Session
from ..repository import user

router=APIRouter(
    prefix="/user",
   tags=['Users']
)

@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(database.get_db)):
    return user.get_user(id,db)
