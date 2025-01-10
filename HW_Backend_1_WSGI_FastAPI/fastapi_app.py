from fastapi import FastAPI
import math

app = FastAPI()

@app.get("/")
async def hello():
    return {"message": "Hello, nfactorial!"}

@app.post("/meaning-of-life")
async def meaning_of_life():
    return {"meaning": "42"}

@app.get("/{num}")
async def calculate_factorial(num: int):
    factorial = math.factorial(num)
    return {"nfactorial": factorial}