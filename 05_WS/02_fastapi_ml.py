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

import pickle

import uvicorn


# Create an APP
app = FastAPI() 


# Create your Functions


# Mainfunction

@app.get("/")
async def root():
    return { "message": "Hallo Fast API"}

 


@app.get("/predict")
async def predict_area_price(area: int, roomcount: int):
    
    # Load Model 
    model = load_model()

    # Predict the price 
    predicted_price = int(model.predict([[area , roomcount]]))

    # Return the predicted Price
    return {
        "area" : area,
        "roomcount": roomcount,
        "price": predicted_price
    }
 



def load_model():
    with open("./models/multivariat_reg_v1.pkl", mode = "rb") as file:
        model = pickle.load(file)

    return model


if __name__ == "__main__":
    uvicorn.run(app)