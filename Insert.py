
# import psycopg2
# import conn as cn
# from fastapi import HTTPException

# def crear_registro_juego(registro):
#     try:
#         conn = cn.connection_db()
#         cur = conn.cursor()
#         query = """
#             INSERT INTO registro_juego (id_jugador, id_palabra, puntuacio, temps_joc, estat_partida)
#             VALUES (%s, %s, %s, %s, %s) RETURNING id_registro, id_jugador, id_palabra, puntuacio, temps_joc, data_hora, estat_partida
#         """
#         cur.execute(query, (registro.id_jugador, registro.id_palabra, registro.puntuacio, registro.temps_joc, registro.estat_partida))
#         nuevo_registro = cur.fetchone()
#         conn.commit()
#         return {
#             "id_registro": nuevo_registro[0],
#             "id_jugador": nuevo_registro[1],
#             "id_palabra": nuevo_registro[2],
#             "puntuacio": nuevo_registro[3],
#             "temps_joc": nuevo_registro[4],
#             "data_hora": nuevo_registro[5].isoformat(),
#             "estat_partida": nuevo_registro[6]
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
#     finally:
#         if conn:
#             cur.close()
#             conn.close()
