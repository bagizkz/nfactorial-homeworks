class UsersRepository:
    def __init__(self):
        self.users = {}
        self.next_user_id = 1

    def create_user(self, email, name, password):
        user = {
            "id": self.next_user_id,
            "email": email,
            "name": name,
            "password": password
        }
        self.users[self.next_user_id] = user
        self.next_user_id += 1
        return user

    def get_user_by_email(self, email):
        for user in self.users.values():
            if user["email"] == email:
                return user
        return None

    def get_user_by_id(self, user_id):
        return self.users.get(user_id)


class FlowersRepository:
    def __init__(self):
        self.flowers = {}
        self.next_flower_id = 1
        self.purchased = {} 

    def create_flower(self, name, quantity, price):
        if quantity <= 0:
            raise HTTPException(status_code=400, detail="Количество цветов больше 0")
        flower = {
            "id": self.next_flower_id,
            "name": name,
            "quantity": quantity,
            "price": price
        }
        self.flowers[self.next_flower_id] = flower
        self.next_flower_id += 1
        return flower

    def get_all_flowers(self):
        return list(self.flowers.values())

    def get_flower_by_id(self, flower_id):
        flower = self.flowers.get(flower_id)
        if not flower:
            raise HTTPException(status_code=404, detail="Цветок не найден")
        return flower

    def update_flower_quantity(self, flower_id, quantity):
        flower = self.get_flower_by_id(flower_id) 
        if flower["quantity"] < quantity:
            raise HTTPException(status_code=400, detail="Недостаточно количества цветов")
        flower["quantity"] -= quantity
        return flower

    def add_flower_to_purchased(self, user_id, flower_id):
        if user_id not in self.purchased:
            self.purchased[user_id] = []
        self.purchased[user_id].append(flower_id)

    def get_purchased_flowers(self, user_id):
        flower_ids = self.purchased.get(user_id, [])
        return [self.flowers[flower_id] for flower_id in flower_ids if flower_id in self.flowers]