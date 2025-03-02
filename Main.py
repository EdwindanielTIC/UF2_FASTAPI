# main.py
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import psycopg2
from conn import connection_db as cn
from create import create_table
import Insert as ins
import read as rd
import Schema_judadores as SHJ
import update as up
import delete as dl


app = FastAPI()

    
def get_db():
    db = cn() # cn() es la función que me devuelve la conexión a la base de datos
    try:
        yield db # me devuelve  la conexión para ser usada en la consultas de los enpints
    finally:
        db.close() # Cierra la conexión automáticamente después de la ejecución
        
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
def puntosdel_jugador(jugadro_id: int, db = Depends(get_db)): ## funcion aprendida , esto hace que mi conexion a mi bbd sea mas rapdio, 
    ## en fatapy me permite la inyeccion de dependecnias, get_db() establece la coneccion a mi bbd que es la que tengo arriba creada, la def get_db()
    ## esto me ayuna a no escribir en cada codigo el db=cn() cursor = db.cursor()
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
    
    
    ## creado delete y update
    
    
@app.put("/actualizar_jugador/{jugador_id}")
def actualizar_jugador(jugador_id: int, jugador: Jugador, db=Depends(get_db)):
    result = up.actualizar_jugador(db, jugador_id, jugador.nombre, jugador.apellido)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Jugador no encontrado")


# Endpoint para actualizar la categoria
@app.put("/actualizar_categoria/{categoria_id}")
def actualizar_categoria(categoria_id: int, categoria: Categoria, db=Depends(get_db)):
    result = up.actualizar_categoria(db, categoria_id, categoria.nombre)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Categoría no encontrada")


#  actualizar  palabra
@app.put("/actualizar_palabra/{palabra_id}")
def actualizar_palabra(palabra_id: int, palabra: Palabra, db=Depends(get_db)):
    result = up.actualizar_palabra(db, palabra_id, palabra.palabra, palabra.categoria_id, palabra.idioma)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Palabra no encontrada")


# Endpoint para eliminar un jugador
@app.delete("/eliminar_jugador/{jugador_id}")
def eliminar_jugador(jugador_id: int, db=Depends(get_db)):
    result = dl.eliminar_jugador(db, jugador_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Jugador no encontrado")


# Endpoint para eliminar una categoría
@app.delete("/eliminar_categoria/{categoria_id}")
def eliminar_categoria(categoria_id: int, db=Depends(get_db)):
    result = dl.eliminar_categoria(db, categoria_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Categoría no encontrada")


# Endpoint para eliminar una palabra
@app.delete("/eliminar_palabra/{palabra_id}")
def eliminar_palabra(palabra_id: int, db=Depends(get_db)):
    result = dl.eliminar_palabra(db, palabra_id)
    if result:
        return result
    raise HTTPException(status_code=404, detail="Palabra no encontrada")