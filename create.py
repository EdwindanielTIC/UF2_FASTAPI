from conn import connection_db

def create_table():
    try:
        conn = connection_db()
        cursor = conn.cursor()
        
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS paraules (
            id SERIAL PRIMARY KEY,
            word TEXT NOT NULL,
            theme TEXT NOT NULL
        );
        '''
        cursor.execute(create_table_query)
        conn.commit()
        
        print("La tabla 'paraules' ha sido creada exitosamente.")
        
 
        
    except Exception as e:
        print(f"Error en la función de crear la tabla: {e}")