from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from hashlib import sha256
from typing import List

from cool_urban_spaces_backend.models import User, UserCreate
import cool_urban_spaces_backend.database


router = APIRouter(
    prefix='/api/user'
)

# Dependency
def get_db():
    db = cool_urban_spaces_backend.database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/{user_id}', response_model=User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db.query(User).filter(User.id == user_id).first()

@router.get('/all', response_model=List[User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(User).offset(skip).limit(limit).all()

@router.post('/add', response_model=UserCreate)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    pwdhash = sha256(user.password.encode('utf-8')).hexdigest()
    db_user = cool_urban_spaces_backend.database.User(name=user.name, pwdhash=pwdhash)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return get_user(db, db_user.id)
