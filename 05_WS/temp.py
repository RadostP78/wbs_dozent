from pydoc import describe
from fastapi import Request

from fastapi import FastAPI, Request

from pydantic import BaseModel
from typing import Optional


    
    


app = FastAPI()

@app.get("/")  
async def root():
    print("Hallo Fast API")