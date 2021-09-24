from typing import List, Optional, Union

from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

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


class MessageBase(BaseModel):
    text: str
    createdAt: int

    class Config:
        orm_mode = True


class Message(MessageBase):
    id: str
    author: User

class MessageCreate(MessageBase):
    author_id: int


