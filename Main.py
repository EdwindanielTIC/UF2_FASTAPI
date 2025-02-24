import db_connect as db
import Schema as sc
import crud as  cr


conn = db.connection_db()

print(cr.create_crud(conn))