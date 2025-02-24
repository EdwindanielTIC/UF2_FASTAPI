import psycopg2

def connection_db():
    
    conn = psycopg2.connect(
        database = "postgres_24255",
        user= "user_postgres1",
        password = "pass_postgres1",
        host = "localhost",
        port = "5433"
        
    )

    print("Estas conectado a la base de datos !!")
    return conn

