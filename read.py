import psycopg2
from conn import connection_db  # Asegúrate de tener esta función en tu archivo de conexión
from Schema_judadores import jugador_schema,categorias_schema


def leer_Jugadores(jugador_id):
    conn = connection_db() ## es muy importante que ponga () porque si no, el execute no me funcionara
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM jugador WHERE id_jugador = %s", (jugador_id,) # es muy importante que ponga la coma si no me darra un error de does not support indexing
    )
    leyendo_jugador = cursor.fetchone()
    conn.commit()
    conn.close()
    
    return jugador_schema(leyendo_jugador)




def leer_categorias(categoria_id):
    conn = connection_db()  # La conexión debe crearse correctamente
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM categorias WHERE id_categorias = %s", (categoria_id,)  # La coma es importante
        )
        leyendo_categoria = cursor.fetchone()

        if not leyendo_categoria:
            return None  # Retorna None si no existe la categoría
        
        return categorias_schema(leyendo_categoria)  # Convierte la categoría a JSON
        
    except psycopg2.Error as e:
        return {"error": str(e)}
    
    finally:
        cursor.close()
        conn.close()
    


def get_categories(db):
    query = "SELECT id_categorias, nombre FROM categorias"
    cursor = db.cursor()
    cursor.execute(query)
    return [{"id_categorias": row[0], "nombre": row[1]} for row in cursor.fetchall()]

## A continuacion creamos la puntuacion de la partidas: 
def obtener_jugadorID(db, jugadro_id: int):
    query = """
        SELECT 
            SUM(puntuacio) as puntos_partidas_actuales,
            COUNT(*) as total_partidas,
            SUM(CASE WHEN estat_partida = 'ganada' THEN 1 ELSE 0 END) as partidas_ganadas,
            MAX(puntuacio) as max_puntos,
            data_hora as fecha_max_puntos
        FROM registro_juego 
        WHERE id_jugador = %s
        GROUP BY id_jugador, data_hora
        ORDER BY max_puntos DESC
        LIMIT 1;
    """
    cursor = db.cursor()
    cursor.execute(query, (jugadro_id,))
    result = cursor.fetchone()

    if result:
        return {
            "puntos_partidas_actuales": result[0] or 0,
            "total_partidas": result[1] or 0,
            "partidas_ganadas": result[2] or 0,
            "partida_amb_mes_punts": {
                "puntos": result[3] or 0,
                "fecha": result[4].strftime("%d/%m/%Y %H:%M") if result[4] else None
            }
        }
    return {
        "puntos_partidas_actuales": 0,
        "total_partidas": 0,
        "partidas_ganadas": 0,
        "partida_amb_mes_punts": {"puntos": 0, "fecha": None}
    }
    
    
    

def get_categories(db):
    query = "SELECT id_categorias, nombre FROM categorias"
    cursor = db.cursor()
    cursor.execute(query)
    return [{"id_categorias": row[0], "nombre": row[1]} for row in cursor.fetchall()]