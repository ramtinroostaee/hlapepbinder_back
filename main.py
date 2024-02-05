import json

from typing import Union

from fastapi import Request, FastAPI
from hlap.hlapepbinder import predict
from pydantic import BaseModel

app = FastAPI()
class Input(BaseModel):
    input: list[float]

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/hlap")
async def get_body(input: Input):
    print(input.input)
    return str(predict(input.input))
