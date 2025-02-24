from typing import Optional
from urllib import response

from fastapi import FastAPI,status
from pydantic import BaseModel

app = FastAPI()

app.title = "Mi primera aplicacion con FastApi de alumnos"

class Item(BaseModel): ## esto lo conecto con el post
    id: int
    name: str
    Apellido: str
    Edad:int
    Direccion : Optional[str] = None
    
items = {
    1: {"id": 25, "name": "Daniel", "apellido": "Ramirez", "edad": 25, "direccion": "Padillas"},
    2: {"id": 30, "name": "Carlos", "apellido": "Gonzales", "edad": 30, "direccion": "Mostoles"},
    3: {"id": 45, "name": "Ana", "apellido": "Martinez", "edad": 58, "direccion": "Argentina"},
}


@app.get("/")
def read_root():
    return {"Hello": "Ejecutando condigo get"}

## CREANDO GET

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        response.status_code = status.HTTP_404_NOT_FOUND
    return {"item": items[item_id]}

## CREANDO POST

@app.post("/Items/")
async def creando_items(item:Item):
    return item







