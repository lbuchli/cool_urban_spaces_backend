from typing import List, Optional

from pydantic import BaseModel



class UserBase(BaseModel):
    id: int

    class Config:
        orm_mode = True

class UserCreate(UserBase):
    name: str
    password: str

class User(UserBase):
    name: str

class SuggestionBase(BaseModel):
    id: str

class SuggestionCreate(SuggestionBase):
    title: str
    description: str
    text: str
    lat: float
    lon: float

class Suggestion(SuggestionBase):
    title: str
    description: str
    text: str
    lat: float
    lon: float
    author_id: int

    class Config:
        orm_mode = True
