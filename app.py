from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hostname")
async def get_hostname():
    hostname = socket.gethostname()
    return {"hostname":hostname}    