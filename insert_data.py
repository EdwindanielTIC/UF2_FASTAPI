import insert_data_csv_to_db as insert_data
import pandas as pd # utilizamos la libreria pandas para que me lea el cvs

def csv_to_json():
    df = pd.read_csv("paraules_temàtica_penjat.csv")## Este nombre debe de ser igual de como se llama el documetneo
    d = df.to_dict(orient='list')

    return d

data = csv_to_json()

for i in range(500):
    insert_data.insert_data_csv_to_db(i, data)