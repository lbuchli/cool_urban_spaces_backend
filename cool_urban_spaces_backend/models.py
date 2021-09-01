from typing import List, Optional, Union

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
    lat: float
    lon: float
    type: int

    class Config:
        orm_mode = True

class SuggestionCreate(SuggestionBase):
    pass

class Suggestion(SuggestionBase):
    id: str
    author_id: Union[int, None]

class CommentBase(BaseModel):
    text: str

    class Config:
        orm_mode = True

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: str
    author_id: Union[int, None]
