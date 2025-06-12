import os

from fastapi import FastAPI
from redis import Redis

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
THE_ENV = os.environ.get("CAIPYRA", "padrao sem graca")


app = FastAPI()
rds = Redis(host=REDIS_HOST)


@app.get("/")
def hello():
    return {"Hello": "Caipyra"}


@app.get("/env")
def environ():
    return {"env": THE_ENV}


@app.get("/store/{item}")
def store_in(item):
    status = rds.set("item", item)
    return {"success": status, "item": item}


@app.get("/show")
def get_from():
    item = rds.get("item")
    return {"item": item}
