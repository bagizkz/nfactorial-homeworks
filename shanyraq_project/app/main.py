from fastapi import FastAPI
from .routers import users, auth, shanyraks
from .database import engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth.router)
app.include_router(shanyraks.router)
app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Qosh keldin. Shanyraq"}