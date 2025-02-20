from sqlalchemy.orm import Session
from models import User, Flower
from fastapi import HTTPException

class UsersRepository:
    def create_user(self, db: Session, email: str, name: str, password: str):
        user = User(email=email, name=name, password=password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_email(self, db: Session, email: str):
        return db.query(User).filter(User.email == email).first()

    def get_user_by_id(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        return user

class FlowersRepository:
    def get_flowers(self, db: Session):
        return db.query(Flower).all()

    def create_flower(self, db: Session, name: str, quantity: int, price: float):
        flower = Flower(name=name, quantity=quantity, price=price)
        db.add(flower)
        db.commit()
        db.refresh(flower)
        return flower

    def update_flower(self, db: Session, flower_id: int, name: str, quantity: int, price: float):
        flower = db.query(Flower).filter(Flower.id == flower_id).first()
        if flower:
            flower.name = name
            flower.quantity = quantity
            flower.price = price
            db.commit()
            db.refresh(flower)
            return flower
        else:
            raise HTTPException(status_code=404, detail="Цветок не найден")

    def delete_flower(self, db: Session, flower_id: int):
        flower = db.query(Flower).filter(Flower.id == flower_id).first()
        if flower:
            db.delete(flower)
            db.commit()
        else:
            raise HTTPException(status_code=404, detail="Цветок не найден")