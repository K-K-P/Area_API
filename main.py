#!/usr/bin/env python

# uvicorn starts the local server at 127.0.0.1:8000
#  It's important to start uvicorn server when current directory is the same as the main.py file's directory

from fastapi import FastAPI
from math import pi

app = FastAPI()





@app.get('/')  # one of request methods (here "GET"); to reach it we place 127.0.0.1:8000 or 127.0.0.1:8000/
async def root():
    return {'message': 'Hello!'}

@app.get('/siema')  # Another endpoint, reached by: 127.0.0.1:8000/siema
async def siema():
    return {'message': 'Siema'}

# Let's create the endpoint which calculates the area of the rectangle

@app.get("/area/rect")
async def read_item(a: int = 0, b: int = 0):
    """Return the area of the rectangle with given a and b. If omitted, default both arguments to 0"""
    return {"area": a * b}  # 127.0.0.1:8000/items/?a=5&b=10

#@app.get('/items/{greeting}')
#async def rectangle_area(greeting):
#    return {'message': greeting}