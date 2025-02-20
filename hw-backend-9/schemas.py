from pydantic import BaseModel

class UserCreate(BaseModel):
    email: str
    name: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: str

    class Config:
        orm_mode = True

class FlowerCreate(BaseModel):
    name: str
    quantity: int
    price: float

class FlowerResponse(BaseModel):
    id: int
    name: str
    quantity: int
    price: float

    class Config:
        orm_mode = True