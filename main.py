
from typing import Union

from fastapi import Request, FastAPI
# from hlap.hlapepbinder import predict

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/hlap")
def the(one: str, two: str):
    return {one: one, two: two}

@app.post("/dummypath")
async def get_body(request: Request):
    return await request.json()



#     return predict(await request.json())
