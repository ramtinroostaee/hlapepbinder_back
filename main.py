
from fastapi import Request, FastAPI
from hlap.hlapepbinder import predict

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/hlap")
async def get_body(request: Request):
    inp = await request.json()
    return {
        key: predict(value) for key, value in inp.items()
    }
