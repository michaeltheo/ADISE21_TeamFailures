from fastapi import APIRouter,Depends
from sqlalchemy.orm.session import Session
from .. import schemas,database
from sqlalchemy.orm import Session
from ..repository import user

router=APIRouter(
    prefix='/Auth',
    tags=['Authentication']
)

@router.post('/login')
def login():
    return 'login'

@router.post('/register',response_model=schemas.ShowUser)
def create_user(request:schemas.User,db:Session=Depends(database.get_db)):
    return user.create_user(request,db)
