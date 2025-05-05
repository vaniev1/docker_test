from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message":"Random Number API"}

@app.get("/random")
def get_random():
    return {"number": random.randint(1,100)}
