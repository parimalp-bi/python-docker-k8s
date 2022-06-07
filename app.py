from urllib import response
from fastapi import FastAPI
import socket
import requests

app = FastAPI()


@app.get("/firstService")
async def root():
    return {"message": "Hello World"}


@app.get("/firstService/hostname")
async def get_hostname():
    hostname = socket.gethostname()
    return {"hostname":hostname}    

@app.get("/firstService/callbackend")
async def get_backendhi():
    response = requests.get('http://python-docker-k8s-backend:4242/backend')
    return response.json()    

@app.get("/firstService/callbackendhost")
async def get_backend_hostname():
    response = requests.get('http://python-docker-k8s-backend:4242/backend/hostname')
    return response.json()        