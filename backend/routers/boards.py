from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.functions import func, mode
from sqlalchemy.sql.expression import func
from .. import schemas, database, models, OAuth2
from ..repository import boards
from typing import List

router = APIRouter(prefix="/boards", tags=["Boards"])


@router.post("/")
def create_board(request: schemas.Boards, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return boards.create_board(request, db)


@router.get("/random", response_model=schemas.Boards)
def get_random_board(db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return boards.get_random_board(db)


@router.get("/", response_model=List[schemas.Boards])
def get_boards(
    db: Session = Depends(database.get_db),
    get_current_user: schemas.User = Depends(OAuth2.get_current_user),
):
    return boards.get_boards(db)


@router.get("/{id}", response_model=schemas.Boards)
def get_board(
    id: UUID,
    db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(OAuth2.get_current_user)
):
    return boards.get_board(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: UUID, request: schemas.Boards, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return boards.update(id, request, db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: UUID, db: Session = Depends(database.get_db), get_current_user: schemas.User = Depends(OAuth2.get_current_user)):
    return boards.destroy(id, db)
