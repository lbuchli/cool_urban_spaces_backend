from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, HTTPException, APIRouter
from hashlib import sha256
from typing import List

from cool_urban_spaces_backend.models import Suggestion, SuggestionCreate
import cool_urban_spaces_backend.database as database

router = APIRouter(
    prefix='/api/suggestion'
)

# Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/all', response_model=List[Suggestion])
def get_suggestions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return db.query(database.Suggestion).offset(skip).limit(limit).all()

@router.get('/{suggestion_id}', response_model=Suggestion)
def get_suggestion(suggestion_id: int, db: Session = Depends(get_db)):
    return db.query(database.Suggestion).filter(database.Suggestion.id == suggestion_id).first()

@router.post('/add', response_model=Suggestion)
def create_suggestion(suggestion: SuggestionCreate, db: Session = Depends(get_db)):
    db_suggestion = database.Suggestion()
    db.add(db_suggestion)
    db.commit()
    db.refresh(db_suggestion)
    return get_suggestion(db_suggestion.id, db)
