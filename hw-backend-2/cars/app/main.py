from fastapi import FastAPI, Response

from .cars import create_cars

cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()


@app.get("/")
def index():
    return Response("<a href='/cars'>Cars</a>")


# (сюда писать решение)


@app.get("/cars")
def get_cars(page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit
    
    paginated_cars = cars[start:end]
    return {"cars": paginated_cars}


@app.get("/cars/{id}")
def get_car_by_id(id: int):
    car = next((car for car in cars if car["id"] == id), None)
    
    if car is None:
        return Response(content="Not found", status_code=404) 
    
    return car

    
    
# (конец решения)
