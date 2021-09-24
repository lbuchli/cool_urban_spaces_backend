from sqlalchemy import create_engine, Integer, String, ForeignKey, Column, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import os

username = "postgres"
password = ""
db_name = "coolcity"

SQLALCHEMY_DATABASE_URL = f"postgresql://{username}:{password}@db/{db_name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    pwdhash = Column(String)

    suggestions = relationship('Suggestion', back_populates='author')
    messages = relationship('Message', back_populates='author')

class Suggestion(Base):
    __tablename__ = "suggestion"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    type = Column(Integer)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    author = relationship('User', back_populates='suggestions')
    messages = relationship('Message', back_populates='suggestion')

class Message(Base):
    __tablename__ = "message"

    id = Column(String, primary_key=True)
    text = Column(String)
    createdat = Column(Integer)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    suggestion_id = Column(Integer, ForeignKey('suggestion.id'), nullable=False)

    author = relationship('User', back_populates='messages')
    suggestion = relationship('Suggestion', back_populates='messages')

