# Cargar librera
from pyspark.sql import SparkSession
# Crear sesión
spark = SparkSession.builder.appName("Data_Wrangling").getOrCreate()

# Importar librerias necesarias para el Cast
from pyspark.sql.types import *

# Cargar el archivo
ReadDF = spark.read.load("C:/Users/joni_/Downloads/HR_Rawdata_Audiencia_20230201.csv",
                         format="csv", sep=",",
                         inferSchema="true",
                         header="true")
print(ReadDF.dtypes)

# Register the DataFrame as a SQL temporary view
ReadDF.createOrReplaceTempView("View")

Consulta = spark.sql("""
SELECT 
COUNT(genero) AS count
FROM View
""")

Consulta.show()

