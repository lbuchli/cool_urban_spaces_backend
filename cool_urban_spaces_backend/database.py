from sqlalchemy import create_engine, Integer, String, ForeignKey, Column, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

SQLALCHEMY_DATABASE_URL = "postgresql://coolcity:intentionally_public_for_local_demo@localhost/coolcity"

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

class Suggestion(Base):
    __tablename__ = "suggestion"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    text = Column(String)
    lat = Column(Float)
    lon = Column(Float)
    author_id = Column(Integer, ForeignKey('user.id'))

    author = relationship('User', back_populates='suggestions')
