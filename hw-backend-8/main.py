from fastapi import FastAPI, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from models import User, Flower, Purchase
from repositories import UsersRepository, FlowersRepository, PurchasesRepository
from database import SessionLocal
from models import Base
from database import engine


app = FastAPI()
Base.metadata.create_all(bind=engine)

import logging



from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


logging.basicConfig(level=logging.DEBUG)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.post("/signup")
def signup(email: str = Form(...), name: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    users_repository = UsersRepository(db)
    user = users_repository.create_user(email, name, password)
    return {"message": "Регистрация успешна", "user": user}


@app.post("/login")
def login(email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    users_repository = UsersRepository(db)
    user = users_repository.get_user_by_email(email)
    if user and pwd_context.verify(password, user.password):
        return {"message": "Авторизация успешна", "user": user}
    raise HTTPException(status_code=401, detail="Неверный email или пароль")


@app.get("/profile")
def profile(user_id: int, db: Session = Depends(get_db)):
    users_repository = UsersRepository(db)
    user = users_repository.get_user_by_id(user_id)
    return {"user": user}


@app.get("/flowers")
def get_flowers(db: Session = Depends(get_db)):
    flowers_repository = FlowersRepository(db)
    flowers = flowers_repository.get_all_flowers()
    return {"flowers": flowers}

@app.post("/flowers")
def add_flower(name: str = Form(...), quantity: int = Form(...), price: float = Form(...), db: Session = Depends(get_db)):
    flowers_repository = FlowersRepository(db)
    flower = flowers_repository.create_flower(name, quantity, price)
    return {"message": "Цветок добавлен", "flower": flower}

@app.patch("/flowers/{flower_id}")
def update_flower(flower_id: int, name: str = Form(...), quantity: int = Form(...), price: float = Form(...), db: Session = Depends(get_db)):
    flowers_repository = FlowersRepository(db)
    flower = flowers_repository.update_flower(flower_id, name, quantity, price)
    if flower:
        return {"message": "Цветок обновлен", "flower": flower}
    raise HTTPException(status_code=404, detail="Цветок не найден")

@app.delete("/flowers/{flower_id}")
def delete_flower(flower_id: int, db: Session = Depends(get_db)):
    flowers_repository = FlowersRepository(db)
    if flowers_repository.delete_flower(flower_id):
        return {"message": "Цветок удален"}
    raise HTTPException(status_code=404, detail="Цветок не найден")