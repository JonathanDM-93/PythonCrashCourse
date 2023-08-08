# Importar las librerías necesarias
# Si funciona perfectamente para la cuenta personal de AWS
import boto3
import psycopg2
import pandas as pd
from numpy import info

# Crea un cliente de Redshift
redshift = boto3.client('redshift')

# Crear una conexión al cluster de Redshift
conexion = psycopg2.connect(
    host='mycluster.cfvkjcuj27ud.us-east-1.redshift.amazonaws.com',
    user='mycluster',
    password='Zamusmetroid10#',
    port=5439,
    database='dev')

# Crear cursor para ejecutar consultas SQL
cursor = conexion.cursor()

# Ejecutar una consulta SQL sobre la tabla mytable
cursor.execute("""SELECT * 
               FROM spectrum_esquema.listings
               LIMIT 10""")

# Recuperar los resultados de la consulta
results = cursor.fetchall()

# Mostrar los resultados
print(results)
print(type(results))

df = pd.DataFrame(results)

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()
