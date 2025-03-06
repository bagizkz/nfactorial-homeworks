from fastapi import FastAPI
from .routers import auth, shanyraks
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Qosh keldin. Shanyraq"}

app.include_router(auth.router)
app.include_router(shanyraks.router)


