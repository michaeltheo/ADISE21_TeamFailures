from fastapi import APIRouter,HTTPException,status,Depends
from sqlalchemy.orm.session import Session
from .. import schemas,models,hashing,database
from sqlalchemy.orm import Session
from ..repository import user

router=APIRouter(
    prefix="/user",
   tags=['Users']
)

@router.post('/',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(database.get_db)):
    return user.create_user(request,db)



@router.get('/{id}',response_model=schemas.ShowUser)
def get_user(id:int,db:Session=Depends(database.get_db)):
    return user.get_user(id,db)
