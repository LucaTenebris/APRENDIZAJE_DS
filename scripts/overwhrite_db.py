import sqlite3
import pandas as pd

#funcion para sobreescribir la base limpia
def sobreescribir_db(db_path,tabla, df_limpio) -> None:
    #conectar a la base de datos sqlite otra vez
    conn = sqlite3.connect(db_path)
    #convertir en df a sql  
    df_limpio.to_sql(tabla,conn, if_exists="replace", index = False)
    #y cerramos la conexion terminamos la diversion
    conn.close()