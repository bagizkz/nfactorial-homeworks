from sqlalchemy.orm import Session
from models import User, Flower, Purchase
from utils import pwd_context 

class UsersRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, email: str, name: str, password: str) -> User:
        hashed_password = pwd_context.hash(password)
        db_user = User(email=email, name=name, password=hashed_password)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

class FlowersRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_flower(self, name: str, quantity: int, price: float) -> Flower:
        db_flower = Flower(name=name, quantity=quantity, price=price)
        self.db.add(db_flower)
        self.db.commit()
        self.db.refresh(db_flower)
        return db_flower

    def get_all_flowers(self) -> list:
        return self.db.query(Flower).all()

    def get_flower_by_id(self, flower_id: int) -> Flower:
        return self.db.query(Flower).filter(Flower.id == flower_id).first()

    def update_flower(self, flower_id: int, name: str, quantity: int, price: float) -> Flower:
        db_flower = self.db.query(Flower).filter(Flower.id == flower_id).first()
        if db_flower:
            db_flower.name = name
            db_flower.quantity = quantity
            db_flower.price = price
            self.db.commit()
            self.db.refresh(db_flower)
            return db_flower
        return None

    def delete_flower(self, flower_id: int) -> bool:
        db_flower = self.db.query(Flower).filter(Flower.id == flower_id).first()
        if db_flower:
            self.db.delete(db_flower)
            self.db.commit()
            return True
        return False

class PurchasesRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_purchase(self, user_id: int, flower_id: int) -> Purchase:
        db_purchase = Purchase(user_id=user_id, flower_id=flower_id)
        self.db.add(db_purchase)
        self.db.commit()
        self.db.refresh(db_purchase)
        return db_purchase

    def get_purchases_by_user(self, user_id: int) -> list:
        return self.db.query(Purchase).filter(Purchase.user_id == user_id).all()