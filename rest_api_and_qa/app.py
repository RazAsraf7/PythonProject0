from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn

class Item(BaseModel):
    name : str
    price : float
    is_offer : Union[bool,None] = None

app = FastAPI()

my_items = {1:{"name":"test1","price":3,"is_offer":True},
            2:{"name":"test2","price":3,"is_offer":True},
            3:{"name":"test3","price":3,"is_offer":True},
            4:{"name":"test4","price":3,"is_offer":True}}

@app.get('/')
async def root():
    return {'message':'Hello World'}

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=5000)
