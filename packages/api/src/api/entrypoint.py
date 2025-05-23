from typing import Union
from prompt import apples, hello

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return hello()

@app.get("/apples")
def read_apples():
    return apples()

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}