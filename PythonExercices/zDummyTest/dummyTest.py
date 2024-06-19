# Cargar librera

from pyspark.sql.functions import broadcast
from pyspark.sql import SparkSession
# Crear sesión
spark = SparkSession.builder.appName("Data_Wrangling").getOrCreate()
# El tipo de archivo PySpark puede leer otros formatos como: json, parquet, orc
# Cargar el archivo

responses_DF = spark.read.load("C:/Users/joni_/Downloads/resp.csv",
                         format="csv", sep="|",
                         inferSchema="true",
                         header="true")

segmentacion_DF = spark.read.load("C:/Users/joni_/Downloads/segmentacion.csv",
                               format="csv", sep="|",
                               inferSchema="true",
                               header="true")

# Aqui el dataframe mas grande es responses_DF y el mas pequeños es segmentacion_DF ayudame a aplicar un brocast inner join a tarves el campo "cliente_id"

result_DF = responses_DF.join(broadcast(segmentacion_DF), responses_DF.cliente_id == segmentacion_DF.cliente_id, 'inner')