from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# база
class Car(BaseModel):
    name: str
    year: int

car_db: List[Car] = []


# list 
@app.get("/cars")
async def list_cars(request: Request):
    return templates.TemplateResponse("cars/list.html", {"request": request, "cars": car_db})



# Search
@app.get("/cars/search")
async def search_cars(request: Request, car_name: Optional[str] = None):
    filtered_cars = [car for car in car_db if car_name.lower() in car.name.lower()] if car_name else []
    return templates.TemplateResponse("cars/search.html", {"request": request, "cars": filtered_cars, "car_name": car_name})


# МNew
@app.get("/cars/new")
async def new_car_form(request: Request):
    return templates.TemplateResponse("cars/new.html", {"request": request})

@app.post("/cars/new")
async def add_new_car(name: str = Form(...), year: int = Form(...)):
    car_db.append(Car(name=name, year=year))
    return RedirectResponse(url="/cars", status_code=303)