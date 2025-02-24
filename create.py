
def create_table(conn):
    conn = conn
    cursor = conn.cursor()
    

    usuarios = ''' CREATE TABLE jugador (
         id_jugador SERIAL PRIMARY KEY,
         nombre VARCHAR(100) NOT NULL,
         apellido VARCHAR(100) NOT NULL
    )
    '''
    
    categorias = '''CREATE TABLE categorias(
        id_categorias SERIAL PRIMARY KEY,
        nombre VARCHAR(50) UNIQUE NOT NULL
        )'''
    
    palabra = '''CREATE TABLE palabras (
        id_palabras SERIAL PRIMARY KEY,
        palabra VARCHAR(100) NOT NULL,
        categoria VARCHAR(50),
        fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        idioma VARCHAR(50) DEFAULT 'Español',
        categoria_id INT,
        FOREIGN KEY (categoria_id) REFERENCES categorias(id)
    )
    '''
    
    registro = ''' CREATE TABLE registro_juego(
        id_registro SERIAL PRIMARY KEY,
        id_jugador INT NOT NULL,
        id_palabra INT NOT NULL,
        puntuacio INT NOT NULL,
        temps_joc INT,
        data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        estat_partida VARCHAR(20) DEFAULT 'en progreso',
        FOREIGN KEY (id_jugador) REFERENCES jugador(id),
        FOREIGN KEY (id_palabra) REFERENCES palabras(id)
        )'''
        
   
    ## Es importante que la tabla que tiene la clave foranea se cree despues de la tabla que tiene la clave primaria, porque si no me dara error
    cursor.execute(usuarios)
    cursor.execute(categorias)
    cursor.execute(palabra)
    cursor.execute(registro)
   
    
    
    conn.commit()
    return "Tablas creadas correctamente"