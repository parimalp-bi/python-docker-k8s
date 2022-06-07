from fastapi import FastAPI
import socket

app = FastAPI()


@app.get("/backend")
async def root():
    return {"message": "Hi From backend service"}


@app.get("/backend/hostname")
async def get_hostname():
    hostname = socket.gethostname()
    return {"backend service host":hostname}    