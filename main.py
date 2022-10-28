from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"Esto es una APP hecho con OKE <3"}


@app.get("/name/{name}")
def hello_name(name: str):
    return {"Hello": name}
