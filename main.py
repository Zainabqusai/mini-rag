
# here we define  a funcation and this funcation we declear a decorator to run the function when the user visits the /hello URL
from fastapi import FastAPI
from base import base_router
from dotenv import load_dotenv
load_dotenv("config.env")
app = FastAPI()

app.include_router(base_router)# i need to tell the app that there is a router in the base.py file u need to include
