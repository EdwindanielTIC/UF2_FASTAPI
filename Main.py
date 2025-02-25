import psycopg2
from psycopg2 import sql
import read as rd
import conn as cn
import create as cr
import db_juego
from typing import Optional
from pydantic import BaseModel
from datetime import datetime
from typing import List
from fastapi import FastAPI, HTTPException
import Insert as ins

app = FastAPI()


if __name__ == "__main__":   
    conn = cn.connection_db()
    cr.create_table(conn)

class usuarios_BM(BaseModel):
    id_jugador: int = None
    nombre: str
    apellido: str

class categoriasBM(BaseModel):
    id_categorias: int = None 
    nombre: str 
    

class Palabra(BaseModel):
    id_palabras: int
    palabra: str
    categoria: Optional[str] = None
    fecha_creacion: Optional[datetime] = None
    idioma: str
    categoria_id: Optional[int] = None ## este punto me dio muchos errores,
    # yo lo habia puesto como categoria_id : int y me devolvia error, al ponerlo Optional me ha devuelto todas las palabras que tengo en mi bbdd.
    
class registro_juego_BM(BaseModel):
    id_registro: int
    id_jugador: int
    id_palabra: int
    puntuacio: int
    temps_joc: Optional[int] = None
    data_hora: datetime
    estat_partida: str
    

# class RegistroJuegoCRealizados(BaseModel):
#     id_jugador: int
#     id_palabra: int
#     puntuacio: int
#     temps_joc: Optional[int] = None
#     estat_partida: str

    
@app.get("/jugadores/{id_jugador}", response_model=usuarios_BM, tags=["GETS"])
def get_jugadores(id_jugador: int):
    try:
        jugador = db_juego.leer_jugador(id_jugador)
        if not jugador:
                raise HTTPException(status_code=404, detail="Jugador con ese ID no exixste")
        return usuarios_BM(**jugador)  
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.get("/palabras/", response_model=List[Palabra], tags=["GETS"])
def obtener_palabras():
    try:
        palabras = rd.leer_palabras()
        if not palabras:
            raise HTTPException(status_code=404, detail="No se han encontrado palabras")
        return palabras
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    
@app.get("/registro_juego/", response_model=List[registro_juego_BM], tags=["GETS"])
def obtener_registros():
    try:
        registros = rd.leer_registros_juego()
        if not registros:
            raise HTTPException(status_code=404, detail="No se han encontrado registros de juego")
        return registros
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))   




##POST

# @app.post("/registro_juego/", response_model=registro_juego_BM, tags=["POSTS"])
# def crear_registro_juego(registro: RegistroJuegoCRealizados):
#     try:
#         nuevo_registro = ins.crear_registro_juego(registro)
#         return nuevo_registro
#     except HTTPException as e:
#         raise e
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))





@app.post("/insertar_jugador", response_model=usuarios_BM, tags=["POST"])
def creando_jugador(jugador : usuarios_BM):
 try:
     nuevo_jugador = db_juego.insertarJugador(
         nombre=jugador.nombre,
         apellido=jugador.apellido)
     print("El jugador se ha insertado correctamente")
     return nuevo_jugador
 except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    

@app.post("/categorias", response_model=categoriasBM, tags=["POST"])
def create_categorias(categoria: categoriasBM):
    try:
        nueva_categoria = db_juego.categorias(categoria.nombre)
        print("Se ha insertado correctamente ")
        return nueva_categoria
       
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        

# @app.post("/palabras", response_model=Palabra , tags=["POST"])
# def create_palabras(palabrasDelJuego: Palabra):
#     try:
#         print(f"Datos recibidos: {palabrasDelJuego}")
#         nueva_palabra = db_juego.palabras(
#             palabra=palabrasDelJuego.palabra,
#             categoria=palabrasDelJuego.categoria,
#             idioma=palabrasDelJuego.idioma,
#             categoria_id=palabrasDelJuego.categoria_id
#         )
#         return nueva_palabra
#     except Exception as e:
#         if "duplicate" in str(e).lower():
#             raise HTTPException(
#                 status_code=400, detail="Esa palabra ya existe en la base de datos"
#             )
#         raise HTTPException(status_code=500, detail=str(e))
    
    




@app.post("/Registro_juego", response_model=registro_juego_BM, tags=["POST"])
def create_registro(registroNuevo : registro_juego_BM):
    try:
        print(f"Registro recibidos: {registroNuevo}")
        nuevoRegistro = db_juego.insertar_registro( ## con lo siguiente hago un registro nuevo de palabra
            id_jugador=registroNuevo.id_jugador,
            id_palabra=registroNuevo.id_palabra,
            puntuacio=registroNuevo.puntuacio,
            estat_partida=registroNuevo.estat_partida
        )
        return nuevoRegistro
    except Exception as e:
        if "duplicate" in str(e).upper():#convierto todas la palbras en mayusulca
            raise HTTPException(
                status_code=400, detail="Este registro ya existe con esa palabra"
            )
        raise HTTPException(status_code=500, detail=str(e))



