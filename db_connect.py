import psycopg2

def connection_db():

    conn = psycopg2.connect(
        database="DbJSON",
        user="postgres",
        password="EdwinDaniel",
        host = "localhost",
        port="5432"
    )


    print("Coneccion establecida correctamente ")
    return conn