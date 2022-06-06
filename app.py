from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/firstService")
async def root():
    return {"message": "Hello World"}


@app.get("/firstService/hostname")
async def get_hostname():
    hostname = socket.gethostname()
    return {"hostname":hostname}    