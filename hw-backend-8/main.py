from fastapi import FastAPI, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from database import get_db, engine
from models import Base
from schemas import UserCreate, UserResponse, FlowerCreate, FlowerResponse
from repositories import UsersRepository, FlowersRepository
from passlib.context import CryptContext

app = FastAPI()

Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
users_repository = UsersRepository()
flowers_repository = FlowersRepository()

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

@app.post("/signup", response_model=UserResponse)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    new_user = users_repository.create_user(db, user.email, user.name, hashed_password)
    return new_user

@app.post("/login")
def login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = users_repository.get_user_by_email(db, email)
    if user and verify_password(password, user.password):
        return {"message": "Успешный вход"}
    else:
        raise HTTPException(status_code=401, detail="Неверный email или пароль")

@app.get("/flowers", response_model=list[FlowerResponse])
def get_flowers(db: Session = Depends(get_db)):
    return flowers_repository.get_flowers(db)

@app.post("/flowers", response_model=FlowerResponse)
def create_flower(flower: FlowerCreate, db: Session = Depends(get_db)):
    return flowers_repository.create_flower(db, flower.name, flower.quantity, flower.price)

@app.patch("/flowers/{flower_id}", response_model=FlowerResponse)
def update_flower(flower_id: int, flower: FlowerCreate, db: Session = Depends(get_db)):
    return flowers_repository.update_flower(db, flower_id, flower.name, flower.quantity, flower.price)

@app.delete("/flowers/{flower_id}")
def delete_flower(flower_id: int, db: Session = Depends(get_db)):
    flowers_repository.delete_flower(db, flower_id)
    return {"message": "Цветок удален"}