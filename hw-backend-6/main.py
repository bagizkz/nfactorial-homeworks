from fastapi import FastAPI, Request, Form, Response, HTTPException, Depends, Cookie
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from typing import List, Dict, Optional
from repositories import UsersRepository, FlowersRepository
from starlette.middleware.sessions import SessionMiddleware
import secrets

secret_key = secrets.token_urlsafe(32)

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=secret_key)

templates = Jinja2Templates(directory="templates")

users_repository = UsersRepository()
flowers_repository = FlowersRepository()

def create_jwt(user_id: int) -> str:
    return str(user_id)


def decode_jwt(token: str) -> Optional[int]:
    try:
        return int(token)
    except ValueError:
        return None



def get_current_user(request: Request) -> Optional[Dict]:
    token = request.cookies.get("jwt")
    if token:
        user_id = decode_jwt(token)
        if user_id:
            return users_repository.get_user_by_id(user_id)
    return None




@app.get("/", response_class=HTMLResponse)
def index(request: Request, user: Dict = Depends(get_current_user)):
    return templates.TemplateResponse("index.html", {"request": request, "user": user})



# signup
@app.get("/signup", response_class=HTMLResponse)
def signup_form(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})

@app.post("/signup")
def signup_process(request: Request, email: str = Form(...), name: str = Form(...), password: str = Form(...)):
    user = users_repository.create_user(email, name, password)
    return RedirectResponse("/login", status_code=303)





# login
@app.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login_process(request: Request, email: str = Form(...), password: str = Form(...)):
    user = users_repository.get_user_by_email(email)
    if user and user["password"] == password:
        jwt_token = create_jwt(user["id"])
        response = RedirectResponse("/profile", status_code=303)
        response.set_cookie(key="jwt", value=jwt_token, httponly=True, samesite="Strict", secure=True)
        return response
    else:
        raise HTTPException(status_code=401, detail="Неверный email или пароль")


@app.get("/profile", response_class=HTMLResponse)
def profile(request: Request, user: Dict = Depends(get_current_user)):
    if not user:
        return RedirectResponse("/login", status_code=303)
    return templates.TemplateResponse("profile.html", {"request": request, "user": user})




# flowers
@app.get("/flowers", response_class=HTMLResponse)
def flowers_page(request: Request, user: Dict = Depends(get_current_user)):
    flowers = flowers_repository.get_all_flowers()
    return templates.TemplateResponse("flowers.html", {"request": request, "flowers": flowers, "user": user})

@app.post("/flowers")
def add_flower(request: Request, name: str = Form(...), quantity: int = Form(...), price: float = Form(...)):
    if quantity <= 0:
        raise HTTPException(status_code=400, detail="Количество цветов должно быть больше 0")
    flowers_repository.create_flower(name, quantity, price)
    return RedirectResponse("/flowers", status_code=303)



# cart
@app.post("/cart/items")
def add_to_cart(request: Request, flower_id: int = Form(...)):
    try:
        flower = flowers_repository.get_flower_by_id(flower_id)
    except HTTPException:
        raise HTTPException(status_code=404, detail="Цветок не найден")

    cart = request.cookies.get("cart", "[]")
    cart = eval(cart)  # Преобразуем обратно в список

    cart.append(flower_id)

    response = RedirectResponse("/flowers", status_code=303)
    response.set_cookie("cart", str(cart))  # Сохраняем корзину в куки как строку

    return response

@app.get("/cart/items", response_class=HTMLResponse)
def cart_items(request: Request, user: Dict = Depends(get_current_user)):
    cart = request.cookies.get("cart", "[]")
    cart = eval(cart)  # Преобразуем обратно в список

    cart_flowers = [flowers_repository.get_flower_by_id(flower_id) for flower_id in cart]
    total_price = sum(flower["price"] for flower in cart_flowers) if cart_flowers else 0

    return templates.TemplateResponse("cart.html", {
        "request": request,
        "cart_flowers": cart_flowers,
        "total_price": total_price,
        "user": user
    })




@app.post("/purchased")
def purchase_items(request: Request, user: Dict = Depends(get_current_user)):
    if not user:
        return RedirectResponse("/login", status_code=303)

    cart_flower_ids = request.cookies.get("cart", "[]")
    cart_flower_ids = eval(cart_flower_ids)  # Преобразуем обратно в список

    for flower_id in cart_flower_ids:
        try:
            flower = flowers_repository.update_flower_quantity(flower_id, 1)  # Уменьшаем на 1
            flowers_repository.add_flower_to_purchased(user["id"], flower_id)
        except HTTPException as e:
            raise HTTPException(status_code=e.status_code, detail=e.detail)

    response = RedirectResponse("/purchased", status_code=303)
    response.set_cookie("cart", "[]")  # Очистим корзину
    return response


@app.get("/purchased", response_class=HTMLResponse)
def purchased_items(request: Request, user: Dict = Depends(get_current_user)):
    if not user:
        return RedirectResponse("/login", status_code=303)
    purchased_flowers = flowers_repository.get_purchased_flowers(user["id"])
    return templates.TemplateResponse("purchased.html", {"request": request, "purchased_flowers": purchased_flowers, "user": user})