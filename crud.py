from db_connect import connection_db
def createTable():
    try:
        conn = connection_db()
        cursor = conn.cursor()
        
        sql= ''' CREATE TABLE users(
            user_id SERIAL PRIMARY KEY,
                user_name VARCHAR(255) NOT NULL,
                user_surname VARCHAR(255) NOT NULL,
                user_age BIGINT NOT NULL,
                user_email VARCHAR(255) NOT NULL)
        '''
        
        cursor.execute(sql)
        conn.commit()
        return "la tabla users ha sido creada exitosamente"
    except Exception as e:
        print(f"Error en la funcion de crear la tabla" + e)
        
        
def update_idAlumne(user_id):
    try:
        conn = connection_db
        cur = conn.cursor()
        idUsuario_query = "SELECT FROM users user_id = %s"
        cur.execute(idUsuario_query,(user_id))
        user_exist = cur.fetchone()
        
        if not user_exist:
            return{"status": -1, "messages" : "El id usuario no existe"}
        
        query = "UPDATE user_id SET user_id = %s WHERE user_id = %s;"
        cur.execute(query,(user_id))
        conn.commit()
    
        return {"status": 1, "message": "id usuario actualizado correctamente"}
    
    except Exception as e:
        print(f"Error en la función update_usuario_id: {e}")
        return {"status": -1, "message": f"Error de conexión: {e}"}
    
    finally:
        conn.close()

    