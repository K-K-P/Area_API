#!/usr/bin/env python

# uvicorn starts the local server at 127.0.0.1:8000
#  It's important to start uvicorn server when current directory is the same as the main.py file's directory

from typing import Optional

from fastapi import FastAPI
from math import pi
from pydantic import BaseModel

app = FastAPI()

@app.get('/')  # one of request methods (here "GET"); to reach it we place 127.0.0.1:8000 or 127.0.0.1:8000/
async def root() -> dict:
    return {'message': 'Hello!'}

@app.get('/siema')  # Another endpoint, reached by: 127.0.0.1:8000/siema
async def siema() -> dict:
    return {'message': 'Siema'}

# Let's create the endpoint which calculates the area of the rectangle

@app.get('/area/rect')
async def read_item(a: int = 0, b: int = 0) -> dict:
    """Return the area of the rectangle with given a and b. If omitted, default both arguments to 0"""
    return {"area": a * b}  # 127.0.0.1:8000/area/rect?a=5&b=10

@app.get('/area/circle')
async def read_item(diameter: int = 0) -> dict:
    """Return the area of the circle with given diameter. If omitted, default both arguments to 0"""
    return {"area": pi*diameter**2/4}  # 127.0.0.1:8000/area/circle?diameter=5

# Using pydantic library to declare JSON Data Models (Data Shapes) for POST operation

class Item(BaseModel):
    # Schema for data to receive from user // Optional arguments don't need to be given
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.post('/items')
async def create_item(item: Item):
    item_dict = item.dict()
    item_dict['price'] = item.price * (1 + item.tax/100)
    return item_dict

