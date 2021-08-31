from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from hashlib import sha256
from typing import List

from cool_urban_spaces_backend.models import User, UserCreate
import cool_urban_spaces_backend.database as database

router = APIRouter(
    prefix='/api/user'
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/all', response_model=List[User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(database.User).offset(skip).limit(limit).all()

@router.get('/{user_id}', response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(database.User).filter(database.User.id == user_id).first()

@router.post('/add', response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    pwdhash = sha256(user.password.encode('utf-8')).hexdigest()
    db_user = database.User(name=user.name, pwdhash=pwdhash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return get_user(db_user.id, db)
