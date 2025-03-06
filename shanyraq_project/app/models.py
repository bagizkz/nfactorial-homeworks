from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.orm import relationship
from .database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    phone = Column(String)
    hashed_password = Column(String)
    name = Column(String)
    city = Column(String)

    shanyraks = relationship("Shanyrak", back_populates="owner")
    comments = relationship("Comment", back_populates="author")

class Shanyrak(Base):
    __tablename__ = "shanyraks"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String)
    price = Column(Integer)
    address = Column(String)
    area = Column(Float)
    rooms_count = Column(Integer)
    description = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="shanyraks")
    comments = relationship("Comment", back_populates="shanyrak")

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    created_at = Column(DateTime)
    author_id = Column(Integer, ForeignKey("users.id"))
    shanyrak_id = Column(Integer, ForeignKey("shanyraks.id"))

    author = relationship("User", back_populates="comments")
    shanyrak = relationship("Shanyrak", back_populates="comments")