
from fastapi import FastAPI
# create a fastapi object 
app = FastAPI()
#@app.get("/") is a decorator that will be called when the user visits the root URL
@app.get("/Welcome")
# define a function that will be called when the user visits the root URL
def home():
    # return a dictionary with a message key and value "Welcome to Mini RAG!"
    return {"message": "Welcome to Mini RAG!"}

@app.get("/hello")
# define a function that will be called when the user visits the /hello URL
def hello(name: str):
    return {"message": f"Hello, {name}!"}
