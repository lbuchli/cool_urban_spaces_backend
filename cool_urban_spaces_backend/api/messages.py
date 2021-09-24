from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, APIRouter, WebSocket
from hashlib import sha256
from typing import List

from cool_urban_spaces_backend.models import Message, MessageCreate
import cool_urban_spaces_backend.database as database

router = APIRouter(
    prefix='/api/message'
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/all', response_model=List[Message])
def get_messages(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(database.Message).offset(skip).limit(limit).all()

@router.websocket("{suggestion_id}/websocket")
async def websocket_endpoint(suggestion_id, websocket: WebSocket, db: Session = Depends(get_db)):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        #TODO: WRITE TO DB
        await websocket.send_text(data)
