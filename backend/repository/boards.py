from uuid import UUID, uuid4
from pydantic.networks import HttpUrl
from sqlalchemy.inspection import inspect
from sqlalchemy.orm.session import Session
from sqlalchemy.sql.elements import Null, and_, or_
from sqlalchemy.sql.functions import mode
from sqlalchemy.sql.operators import isnot
from backend import schemas, models, database
from fastapi import HTTPException, status
from sqlalchemy.sql.expression import asc, desc, false, func
from typing import List
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


def create_board(request: schemas.Boards, db: Session):
    new_board = models.Boards(
        id=uuid4(),
        creator_id=request.creator_id,
        players=request.players,
        board=[],
        isFull=False,
    )
    db.add(new_board)
    db.commit()
    db.refresh(new_board)
    json_board = jsonable_encoder(new_board)
    return JSONResponse(content=json_board)


def get_random_board(db: Session):
    # find a board with 1 player already inside
    # board = db.query(models.Boards).order_by(asc(models.Boards.players)).first()
    board = db.query(models.Boards).filter(models.Boards.isFull == False).first()
    # models.Boards.players.name. !=None).first()

    if not board:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"There are no boards with 1 player",
        )
    json_board = jsonable_encoder(board)
    return json_board


def update(id: UUID, request: schemas.Boards, db: Session):
    board = db.query(models.Boards).filter(models.Boards.id == id)
    board_model = board.first()
    if not board_model:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Board with id {id} was not found",
        )
    if not board_model.isFull:
        for item in request:
            if item[1] is not None:
                print(item[1])
                board.update({item[0]: item[1]})
    if len(board_model.players) == 2:
        board.update({"isFull": True})
    db.commit()
    return request


def destroy(id: UUID, db: Session):
    board = db.query(models.Boards).filter(models.Boards.id == id)
    if not board.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Board with id {id} not found",
        )
    board.delete(synchronize_session=False)
    db.commit()
    return "done"


def get_boards(db: Session):
    boards = db.query(models.Boards).all()
    if not boards:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"There are no boards"
        )
    return boards


def get_board(id: UUID, db: Session):
    board = db.query(models.Boards).filter(models.Boards.id == id).first()
    if not board:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Board with the Uuid {id} is not available",
        )
    return board
