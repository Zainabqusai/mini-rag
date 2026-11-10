from fastapi import APIRouter
import os 
base_router = APIRouter(
    prefix="/api/v1",
    #add tag name 
    tags=["api_v1"]
)

@base_router.get("/")
def welcome():
    app_name=os.getenv("APP_NAME")
    app_version=os.getenv("APP_VERSION")
    return {
        "app_name": app_name,
        "app_version": app_version,
    }

#each routes about the same thing we will put it in the same file 
# any app must response to the default route

