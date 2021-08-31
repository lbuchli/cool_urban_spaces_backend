from typing import List, Optional

from pydantic import BaseModel

class UserBase(BaseModel):
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    name: str
    password: str

class User(UserBase):
    id: int
    name: str

class SuggestionBase(BaseModel):
    title: str
    description: str
    text: str
    lat: float
    lon: float

    class Config:
        orm_mode = True

class SuggestionCreate(SuggestionBase):
    pass

class Suggestion(SuggestionBase):
    id: str
    author_id: int
