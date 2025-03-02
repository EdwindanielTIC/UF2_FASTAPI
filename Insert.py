import psycopg2
from conn import connection_db  # Asegúrate de tener esta función en tu archivo de conexión
import Schema_judadores as sch


def insertar_jugador(jugador):
    conn = connection_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO jugador (nombre, apellido) VALUES (%s, %s) RETURNING id_jugador,nombre,apellido",
        (jugador.nombre, jugador.apellido)
    )
    datos_jugador = cursor.fetchone()
    conn.commit()
    conn.close()
    
    return sch.jugador_schema(datos_jugador)


    
        
def registrar_intentos(db):
    query = "INSERT INTO registro_juego (id_jugador, id_palabra, puntuacio, temps_joc) VALUES (1, 1, 0, 0) RETURNING id_registro"
    cursor = db.cursor()
    cursor.execute(query)
    db.commit()
    return {"id_registro": cursor.fetchone()[0]}


## a continuacion he hecho la funcion de insertar 

def crear_categoria(db, nombre: str):
    query = "INSERT INTO categorias (nombre) VALUES (%s) RETURNING id_categorias, nombre"
    cursor = db.cursor()
    cursor.execute(query, (nombre,))
    db.commit()
    return {"id_categorias": cursor.fetchone()[0], "nombre": nombre}



def registrar_intento(db, jugador_id: int, palabra_id: int, puntos: int, tiempo_jugado: int, ganado: bool = False):
    estado_partida = "ganada" if ganado else "en progreso"
    
    query = """
        INSERT INTO registro_juego (id_jugador, id_palabra, puntuacio, temps_joc, estat_partida) 
        VALUES (%s, %s, %s, %s, %s) 
        RETURNING id_registro
    """
  
    cursor = db.cursor()
    cursor.execute(query, (jugador_id, palabra_id, puntos, tiempo_jugado, estado_partida))
    db.commit()
    return {"id_registro": cursor.fetchone()[0]}