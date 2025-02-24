import psycopg2

def insert_data_csv_to_db(pos, data):
    try:
        conn = psycopg2.connect(
            database="actividad10",  # Asegúrate de que esta base de datos existe en pgAdmin
            password="pass_postgres1",
            host="localhost",
            user="user_postgres1",
            port="5433"
        )
        cur = conn.cursor()

        # Verificamos que las claves existen antes de acceder a ellas
        if "WORD" not in data or "THEME" not in data:
            print("Error: Claves 'WORD' o 'THEME' no encontradas en los datos.")
            return {"Message": "Error en los datos"}

        sql = "INSERT INTO paraules (word, theme) VALUES (%s, %s);"
        values = (data["WORD"][pos], data["THEME"][pos])

        cur.execute(sql, values)
        conn.commit()

        cur.close()
        conn.close()

        return {"Message": "Data inserted successfully"}
    
    except Exception as e:
        print(f"Error al insertar datos: {e}")
        return {"Message": "Error al insertar datos"}
