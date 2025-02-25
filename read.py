import psycopg2
import conn as cn
from fastapi import HTTPException
import alumne_Schema

def leer_palabras():
    try:
        conn = cn.connection_db()
        cur = conn.cursor()
        query = "SELECT id_palabras, palabra, categoria, fecha_creacion, idioma, categoria_id FROM palabras"
        cur.execute(query)
        palabras = cur.fetchall()
       
        if not palabras:
            return []
        devolver_palabra = [
            {
                "id_palabras": row[0],
                "palabra": row[1],
                "categoria": row[2],
                "fecha_creacion": row[3],
                "idioma": row[4],
                "categoria_id": row[5] if row[5] is not None else None
            }
            for row in palabras
        ]
       
        return devolver_palabra
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if conn:
            cur.close()
            conn.close()
            

def leer_registros_juego():
    try:
        conn = cn.connection_db()
        cur = conn.cursor()
        query = "SELECT id_registro, id_jugador, id_palabra, puntuacio, temps_joc, data_hora, estat_partida FROM registro_juego"
        cur.execute(query)
        registros = cur.fetchall()
        
        if not registros:
            return []
        
        devolver_registro = [
            {
                "id_registro": row[0],
                "id_jugador": row[1],
                "id_palabra": row[2],
                "puntuacio": row[3],
                "temps_joc": row[4] if row[4] is not None else None,
                "data_hora": row[5].isoformat(),
                "estat_partida": row[6]
            }
            for row in registros
        ]
        return devolver_registro
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        if conn:
            cur.close()
            conn.close()