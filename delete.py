def eliminar_jugador(db, jugador_id: int):
    query = "DELETE FROM jugador WHERE id_jugador = %s RETURNING id_jugador"
    cursor = db.cursor()
    cursor.execute(query, (jugador_id,))
    db.commit()
    
    result = cursor.fetchone()
    return {"mensaje": "Jugador eliminado"} if result else None


def eliminar_categoria(db, categoria_id: int):
    query = "DELETE FROM categorias WHERE id_categorias = %s RETURNING id_categorias"
    cursor = db.cursor()
    cursor.execute(query, (categoria_id,))
    db.commit()
    
    result = cursor.fetchone()
    return {"mensaje": "Categoría eliminada"} if result else None


def eliminar_palabra(db, palabra_id: int):
    query = "DELETE FROM palabras WHERE id_palabras = %s RETURNING id_palabras"
    cursor = db.cursor()
    cursor.execute(query, (palabra_id,))
    db.commit()
    
    result = cursor.fetchone()
    return {"mensaje": "Palabra eliminada"} if result else None
