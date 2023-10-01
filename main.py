from fastapi import FastAPI

from routers import test

app = FastAPI()

app.include_router(test.router)


@app.get("/")
def read_root():
    return {"Hello": "World!"}
