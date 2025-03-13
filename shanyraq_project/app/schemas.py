from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional

class UserBase(BaseModel):
    username: str
    phone: str
    name: str
    city: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    model_config = {"from_attributes": True}

class UserUpdate(BaseModel):
    username: Optional[str] = None
    phone: Optional[str] = None
    name: Optional[str] = None
    city: Optional[str] = None
    password: Optional[str] = None

class ShanyrakBase(BaseModel):
    type: str
    price: int
    address: str
    area: float
    rooms_count: int
    description: str

class ShanyrakCreate(ShanyrakBase):
    pass

class Shanyrak(ShanyrakBase):
    id: int
    owner_id: int
    total_comments: int = 0

    model_config = {"from_attributes": True}

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    created_at: datetime
    author_id: int
    model_config = {"from_attributes": True}

class CommentList(BaseModel):
    comments: List[Comment]

class FavoriteShanyrak(BaseModel):
    id: int
    address: str

    model_config = {"from_attributes": True}

class FavoriteShanyrakList(BaseModel):
    shanyraks: List[FavoriteShanyrak]

class ShanyrakSearchResult(BaseModel):
    id: int
    type: str
    price: int
    address: str
    area: float
    rooms_count: int

    model_config = {"from_attributes": True}

class ShanyrakSearchResultList(BaseModel):
    total: int
    objects: List[ShanyrakSearchResult]