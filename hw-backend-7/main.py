from fastapi import FastAPI, Request, Form, Response, HTTPException, Depends, Cookie
from fastapi.responses import JSONResponse
from typing import List, Dict, Optional
from repositories import UsersRepository, FlowersRepository
import jwt
import secrets
from datetime import datetime, timedelta
import json
from passlib.context import CryptContext

SECRET_KEY = secrets.token_urlsafe(32)
ALGORITHM = "HS256"
TOKEN_EXPIRATION_HOURS = 1

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app = FastAPI()

users_repository = UsersRepository()
flowers_repository = FlowersRepository()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_jwt(user_id: int) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(hours=TOKEN_EXPIRATION_HOURS)
    }
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_jwt(token: str) -> Optional[int]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("user_id")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Токен истёк")
    except jwt.PyJWTError:
        return None


def get_current_user(request: Request) -> Optional[Dict]:
    token = request.headers.get("Authorization")
    if token and token.startswith("Bearer "):
        token = token.split(" ")[1]
        user_id = decode_jwt(token)
        if user_id:
            return users_repository.get_user_by_id(user_id)
    return None


@app.get("/")
def index(user: Dict = Depends(get_current_user)):
    if not user:
        return JSONResponse(content={"message": "Добро пожаловать"})
    return {"message": f"Добро пожаловать, {user['name']}!"}


@app.post("/signup")
def signup(email: str = Form(...), name: str = Form(...), password: str = Form(...)):
    hashed_password = hash_password(password)
    user = users_repository.create_user(email, name, hashed_password)
    return {"message": "Регистрация успешна", "user": user}


@app.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    user = users_repository.get_user_by_email(email)
    if user and verify_password(password, user["password"]):
        jwt_token = create_jwt(user["id"])
        return {"access_token": jwt_token, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Неверный email или пароль")


@app.get("/profile")
def profile(user: Dict = Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="Пользователь не авторизован")
    return {"user": user}


@app.get("/flowers")
def get_flowers():
    flowers = flowers_repository.get_all_flowers()
    return {"flowers": flowers}


@app.post("/flowers")
def add_flower(name: str = Form(...), quantity: int = Form(...), price: float = Form(...)):
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Количество цветов должно быть больше 0")
    flower = flowers_repository.create_flower(name, quantity, price)
    return {"message": "Цветок добавлен", "flower": flower}


@app.post("/cart/items")
def add_to_cart(request: Request, flower_id: int = Form(...)):
    flower = flowers_repository.get_flower_by_id(flower_id)
    if not flower:
        raise HTTPException(status_code=404, detail="Цветок не найден")

    try:
        cart = json.loads(request.cookies.get("cart", "[]"))
    except json.JSONDecodeError:
        cart = []

    cart.append(flower_id)

    response = JSONResponse(content={"message": "Цветок добавлен в корзину"})
    response.set_cookie("cart", json.dumps(cart))
    return response


@app.get("/cart/items")
def get_cart_items(request: Request):
    try:
        cart = json.loads(request.cookies.get("cart", "[]"))
    except json.JSONDecodeError:
        cart = []

    cart_flowers = [flowers_repository.get_flower_by_id(flower_id) for flower_id in cart]
    total_price = sum(flower["price"] for flower in cart_flowers) if cart_flowers else 0
    return {"cart_flowers": cart_flowers, "total_price": total_price}


@app.post("/purchased")
def purchase_items(request: Request, user: Dict = Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="Пользователь не авторизован")

    try:
        cart_flower_ids = json.loads(request.cookies.get("cart", "[]"))
    except json.JSONDecodeError:
        cart_flower_ids = []

    for flower_id in cart_flower_ids:
        flowers_repository.update_flower_quantity(flower_id, 1)
        flowers_repository.add_flower_to_purchased(user["id"], flower_id)

    response = JSONResponse(content={"message": "Покупка завершена"})
    response.set_cookie("cart", "[]")
    return response


@app.get("/purchased")
def get_purchased_items(user: Dict = Depends(get_current_user)):
    if not user:
        raise HTTPException(status_code=401, detail="Пользователь не авторизован")
    purchased_flowers = flowers_repository.get_purchased_flowers(user["id"])
    return {"purchased_flowers": purchased_flowers}