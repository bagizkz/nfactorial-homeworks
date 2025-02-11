from fastapi import HTTPException
from typing import Dict, List
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


class UsersRepository:
    def __init__(self):
        self.users: Dict[int, Dict] = {}
        self.next_user_id: int = 1

    def create_user(self, email: str, name: str, password: str) -> Dict:
        user = {
            "id": self.next_user_id,
            "email": email,
            "name": name,
            "password": password
        }
        self.users[self.next_user_id] = user
        self.next_user_id += 1
        return user

    def get_user_by_email(self, email: str) -> Dict:
        for user in self.users.values():
            if user["email"] == email:
                return user
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    def get_user_by_id(self, user_id: int) -> Dict:
        user = self.users.get(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Пользователь не найден")
        return user


class FlowersRepository:
    def __init__(self):
        self.flowers: Dict[int, Dict] = {}
        self.next_flower_id: int = 1
        self.purchased: Dict[int, List[int]] = {}

    def create_flower(self, name: str, quantity: int, price: float) -> Dict:
        if quantity <= 0:
            raise HTTPException(status_code=400, detail="Количество цветов должно быть больше 0")
        flower = {
            "id": self.next_flower_id,
            "name": name,
            "quantity": quantity,
            "price": price
        }
        self.flowers[self.next_flower_id] = flower
        self.next_flower_id += 1
        return flower

    def get_all_flowers(self) -> List[Dict]:
        return list(self.flowers.values())

    def get_flower_by_id(self, flower_id: int) -> Dict:
        flower = self.flowers.get(flower_id)
        if not flower:
            raise HTTPException(status_code=404, detail="Цветок не найден")
        return flower

    def update_flower_quantity(self, flower_id: int, quantity: int) -> Dict:
        flower = self.get_flower_by_id(flower_id)
        if flower["quantity"] < quantity:
            raise HTTPException(status_code=400, detail="Недостаточно количества цветов")
        flower["quantity"] -= quantity
        return flower

    def add_flower_to_purchased(self, user_id: int, flower_id: int):
        if user_id not in self.purchased:
            self.purchased[user_id] = []
        self.purchased[user_id].append(flower_id)

    def get_purchased_flowers(self, user_id: int) -> List[Dict]:
        flower_ids = self.purchased.get(user_id, [])
        return [self.flowers[flower_id] for flower_id in flower_ids if flower_id in self.flowers]
