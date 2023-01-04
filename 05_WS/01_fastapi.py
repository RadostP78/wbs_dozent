""" 
> pip install fastapi
> pip install uvicorn

> uvicorn 01_fastapi:app --reload

"""

from pydoc import describe
from fastapi import Request

from fastapi import FastAPI, Request

from pydantic import BaseModel
from typing import Optional





# Create an APP
app = FastAPI() 


# Create your Functions


# Mainfunction

@app.get("/")
async def root():
    print("Hallo Fast API")


# http://127.0.0.1:8000/items/banana ---> bad   
# http://127.0.0.1:8000/items/70 ---> good

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    print("Item id:", item_id)


@app.get("/getuserinfo/{user_id}")
async def get_user_info(user_id: int):
    return { "user_id": user_id }



# 127.0.0.1:8000/getadvancedinfo?id=1&name=thomas ---> good
# http://127.0.0.1:8000/getadvancedinfo?id=a&name=thomas ---> bad
# 127.0.0.1:8000/getadvancedinfo?id=1&name=2 ---> good
# Alternative
@app.get("/getadvancedinfo")
async def get_advanced_info(id:int, name: str):
    return {
        "status" : "Succes",
        "user_id": id, 
        "user_name": name }

