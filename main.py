
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Mini RAG!"}

@app.get("/hello")
def hello(name: str):
    return {"message": f"Hello, {name}!"}
