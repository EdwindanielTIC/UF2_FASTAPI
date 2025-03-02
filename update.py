def actualizar_jugador(db, jugador_id: int, nombre: str, apellido: str):
    query = """
        UPDATE jugador
        SET nombre = %s, apellido = %s
        WHERE id_jugador = %s
        RETURNING id_jugador, nombre, apellido
    """
    cursor = db.cursor()
    cursor.execute(query, (nombre, apellido, jugador_id))
    db.commit()
    
    result = cursor.fetchone()
    if not result:
        return None
    return {"id_jugador": result[0], "nombre": result[1], "apellido": result[2]}


def actualizar_categoria(db, categoria_id: int, nuevo_nombre: str):
    query = """
        UPDATE categorias
        SET nombre = %s
        WHERE id_categorias = %s
        RETURNING id_categorias, nombre
    """
    cursor = db.cursor()
    cursor.execute(query, (nuevo_nombre, categoria_id))
    db.commit()
    
    result = cursor.fetchone()
    if not result:
        return None
    return {"id_categorias": result[0], "nombre": result[1]}


def actualizar_palabra(db, palabra_id: int, nueva_palabra: str, nueva_categoria_id: int, nuevo_idioma: str):
    query = """
        UPDATE palabras
        SET palabra = %s, categoria_id = %s, idioma = %s
        WHERE id_palabras = %s
        RETURNING id_palabras, palabra, categoria_id, idioma
    """
    cursor = db.cursor()
    cursor.execute(query, (nueva_palabra, nueva_categoria_id, nuevo_idioma, palabra_id))
    db.commit()
    
    result = cursor.fetchone()
    if not result:
        return None
    return {
        "id_palabras": result[0],
        "palabra": result[1],
        "categoria_id": result[2],
        "idioma": result[3],
    }
