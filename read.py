import psycopg2
import conn as cn
import alumne_Schema
from fastapi import HTTPException

def leer_palabras():
    try:
        conn = cn.connection_db()
        cur = conn.cursor()
        query = "SELECT * FROM palabras"
        cur.execute(query)
        palabras = cur.fetchall()
        
        if not palabras:
            raise HTTPException(status_code=404, detail="No se encontraron palabras")
        
        # Transformar cada fila usando la función `palabra` del esquema
        palabras_transformadas = [alumne_Schema.palabra(palabra) for palabra in palabras]
        return palabras_transformadas
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    finally:
        if conn:
            cur.close()
            conn.close()
