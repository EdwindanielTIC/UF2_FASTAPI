import psycopg2
import conn as cn
import alumne_Schema 

def leer_jugador(id_jugador : int):
    try:
                conn = cn.connection_db()
                cur = conn.cursor()
                query = "SELECT id_jugador,nombre,apellido FROM jugador WHERE id_jugador = %s"
                cur.execute(query, (id_jugador,))
                jugador = cur.fetchone()
                
                if not jugador:
                    return "No se ha encontrado el jugador"
                              
                return alumne_Schema.jugador_schema(jugador)
                
    except Exception as e:
        raise Exception(f"NO se ha podido realizar la consulta")
    

def insertarJugador(nombre: str, apellido: str):
    try:
        conn = cn.connection_db()
        cur = conn.cursor()
        query = "INSERT INTO jugador (nombre, apellido) VALUES (%s, %s) RETURNING id_jugador"
        cur.execute(query, (nombre, apellido))
        # Ejecutar la consulta e intentar recuperar el ID generado automáticamente
        
        insertando_jugador = (cur.fetchone()[0],nombre, apellido)  # aqui debo de poner el cur.fetchone + el nombre y apellido porque la funcion esta esperando 3 valores, si no me dara errors
        conn.commit()
        
        print("Se ha insertado correctamente")
        return alumne_Schema.jugador_schema(insertando_jugador)
        
    except Exception as e:
        raise Exception(f"NO se ha podido insertar el jugador: {e}")
    finally:
        cur.close()
        conn.close()

    
    
    
def categorias(nombre: str):
    try:
        conn = cn.connection_db()
        cur = conn.cursor()
        
        query_categorias = "INSERT INTO categorias (nombre) VALUES (%s) RETURNING id_categorias"
        cur.execute(query_categorias, (nombre,))
        
        id_categoria = cur.fetchone()[0]
        conn.commit()
        
        print("Se insertado correctamente")
        return alumne_Schema.categorias_schema((id_categoria,nombre))
      
    except Exception as e:
        raise Exception(f"NO se ha podido realizar la consulta {e} ")
    

def palabras(palabra: str, categoria: str, idioma: str, categoria_id: int):
    try:
        conn = cn.connection_db()
        cur = conn.cursor()
        
        query_palabras = """
        INSERT INTO palabras (palabra, categoria, idioma, categoria_id) 
        VALUES (%s, %s, %s, %s) RETURNING *
        """
        values = (palabra, categoria, idioma, categoria_id)
        
        # me imprimirar la consulta y los valores para controlar los posibles errores 
        print(f"Ejecutando consulta: {query_palabras} con valores {values}")
        
        cur.execute(query_palabras, values)
        conn.commit()
        
        nueva_palabra = cur.fetchone()
        return alumne_Schema.palabra(nueva_palabra)
    except Exception as e:
        raise Exception(f"NO se ha podido realizar la consulta: {e}")
    finally:
        cur.close()
        conn.close()
    
    
def insertar_registro(id_jugador: int, id_palabra: int, puntuacio: int, temps_joc: int = None, estat_partida: str = "en progreso"):
    try:
        conn = cn.connection_db()  
        cur = conn.cursor()

        query_registro = """
        INSERT INTO registro_juego (id_jugador, id_palabra,puntuacio,temps_joc,estat_partida) 
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (id_jugador, id_palabra, puntuacio, temps_joc, estat_partida)


        cur.execute(query_registro, values)
        conn.commit()
        
        nuevo_registro = cur.fetchone()
        return alumne_Schema.registro_juego_Schema(nuevo_registro)

    except Exception as e:
        conn.rollback()
        raise Exception(f"Error al insertar registro: {e}")
    finally:
        cur.close()
        conn.close()
    

