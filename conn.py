import psycopg2

def connection_db():
    
   conn = psycopg2.connect(
       database = "actividad10", ## este sera el nombre que tendra mi base de dato en gpadmi, dentro de Database, tendre que crear este nombre
       password = "pass_postgres1",
       host = "localhost",
       user="user_postgres1",
       port = "5433"
   )

   print("Conexion establecida correctamente")
   return conn