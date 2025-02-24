from fastapi import FastAPI
from typing import List
from opciones_sc import options_schema
import read 
import conn as cn
import create as cr
import insert_data 

app = FastAPI()

# Conectar a la base de datos y crear la tabla al iniciar el script
conn = cn.connection_db()
cr.create_table()
print(insert_data)

@app.get("/")
async def root():
    return {"message": "Actividad 10 FastAPI"}

@app.get("/tematicas_juego", response_model=List[dict])
async def obtener_opciones():
    return options_schema(read.read_db())


# con lo siguiente hacmeos un get de opciones para que me devuleva la palabra
@app.get("/penjat/tematica/{option}", response_model=List[dict])
async def get_word(option: str):
    word = options_schema(read.read_word_db(option))
    print("\nIMPRESSIÓ WORD del mètode GET_WORD")
    print(type(word))
    print(word)
    
    return word  