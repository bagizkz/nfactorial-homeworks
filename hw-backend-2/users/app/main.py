from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates

from .users import create_users

users = create_users(100)  # Здесь хранятся список пользователей
app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# (сюда писать решение)


@app.get("/users")
def index(request: Request):
    sorted_users = sorted(users, key=lambda user: user["id"])
    return templates.TemplateResponse("users/index.html", {"request": request, "users": sorted_users})

@app.get("/users/{id}")
def user_detail(request: Request, id: int):
    user = next((u for u in users if u["id"] == id), None)
    if user:
        return templates.TemplateResponse("users/user.html", {"request": request, "user": user})
    return {"error": "User not found"}

# (конец решения)
