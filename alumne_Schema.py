from pydantic import BaseModel
from datetime import datetime


def jugador_schema(jugador):
    return{
        "id_jugador" : jugador[0],
        "nombre" : jugador[1],
        "apellido" : jugador[2]
    }


def categorias_schema(categorias):
    return{
        "id_categorias": categorias[0],
        "nombre" : categorias[1]
    }
    
def palabra(palabra):
    return{
        "id_palabras": palabra[0],
        "palabra": palabra[1],
        "categoria": palabra[2],
        "fecha_creacion": palabra[3],
        "idioma": palabra[4],
        "categoria_id": palabra[5],
    }
    

def registro_juego_Schema(registro):
    return{
        "id_registro": registro[0],
        "id_jugador": registro[1],
        "id_palabra": registro[2],
        "puntuacio": registro[3],
        "temps_joc": registro[4],
        "data_hora": registro[5],
        "estat_partida": registro[6]
    }
    
    


