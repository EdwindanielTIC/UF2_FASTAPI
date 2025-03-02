# main.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from conn import connection_db as cn
from create import create_table
import Insert as ins
import read as rd
import Schema_judadores as SHJ


app = FastAPI()

    
def get_db():
    db = cn()
    try:
        yield db
    finally:
        db.close()
        
##Creamon los BASEMODEL
class Jugador(BaseModel):
    nombre: str
    apellido: str

class Categoria(BaseModel):
    nombre: str

class Palabra(BaseModel):
    palabra: str
    categoria_id: int
    idioma: str = "Español"

class RegistroJuego(BaseModel):
    id_jugador: int
    id_palabra: int
    puntuacio: int
    temps_joc: int
    estat_partida: str = "en progreso"
    
  
  
@app.get("/Comneçar el joc/")
def comenzar_joc():
    return {"message": "Començar partida"}

@app.get("/renderitzar text/")
def rederitzar_elText():
    return {"text": "C o m e n ç a r   p a r t i d a"}




@app.get("/abecedario/", response_model=list[str])
def get_abecedario(language: str = "es"):
    abecedario = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    if language == "es":
        abecedario.extend(["Ñ", "Á", "É", "Í", "Ó", "Ú"])
    elif language == "ca":
        abecedario.extend(["Ç", "À", "È", "Ò", "Ù"])
    return abecedario

## get de devolver los puntos de mi partida: 

@app.post("/registrar_Intentos/")
def registrar_Intentos(jugador_id: int, palabra_id: int, puntos: int, tiempo_jugado: int, ganado: bool = False, db = Depends(get_db)):
  return ins.registrar_intento(db, jugador_id, palabra_id, puntos, tiempo_jugado, ganado)



@app.get("/get_info_jugador/{jugadro_id}")
def puntosdel_jugador(jugadro_id: int, db = Depends(get_db)):
    stats = rd.obtener_jugadorID(db, jugadro_id)
    return {
        "jugador": f"Jugador {jugadro_id}",
        "puntos_partidas_actuales": stats["puntos_partidas_actuales"],
        "total_partidas": stats["total_partidas"],
        "partidas_ganadas": stats["partidas_ganadas"],
        "partida_amb_mes_punts": f"{stats['partida_amb_mes_punts']['fecha']} - {stats['partida_amb_mes_punts']['puntos']} punts"
    }




  
# Endpoints para insertar jugadores
@app.post("/insertar_jugador/")
def crear_jugador(jugador: Jugador):
    return ins.insertar_jugador(jugador)

@app.get("/obtener_jugadores/{jugador_id}")
def obtener_jugador(jugador_id: int):
    return rd.leer_Jugadores(jugador_id)
    

# Endpoints para Categorias
@app.post("/insertar_categorias/")
def crear_categoria(categoria: Categoria, db=Depends(get_db)):
    try:
        return ins.crear_categoria(db, categoria.nombre)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    ## si quiero que me de el error en fastapy y no en consola, debo de poner este raise HTTPException para que me devuevla el error si 
    #ya es existe , lo que hay en la consulta de insertar_categorias es el error que me devolvera




@app.get("/obtener_categorias_id/{categoria_id}")
def obtener_categoria(categoria_id: int):
    try:
        resultado = rd.leer_categorias(categoria_id)
        if resultado is None:
            raise HTTPException(status_code=404, detail="La categoría con ese ID no existe")
        return resultado
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}") 

@app.get("/mostrar_todas_categories/")
def get_categories(db = Depends(get_db)):
    try:
        return rd.get_categories(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))