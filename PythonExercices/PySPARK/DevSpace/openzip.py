#import pandas as pd
#data = pd.read_csv('C:/Users/joni_/Downloads/tmpbt5gy53v.csv.gz', compression='gzip', error_bad_lines=False)

# print(data) # Imprime un rango de valores de como se ve la información.
# print(data.dtypes) # Tipo de datos que tienen las columnas datatype.
# print(data.shape) # Numero de renglones y columnas que contiene el archivo.

# Cargar el archivo de la siguiente ruta en s3
# Cargar librera
from pyspark.sql import SparkSession
# Crear sesión
spark = SparkSession.builder.appName("Data_Wrangling").getOrCreate()

# Importar librerias necesarias para el Cast
# from pyspark.sql.types import *

# Cargar el archivo Parquet
ReadDFParquet = spark.read.parquet("C:/Users/joni_/Downloads/20230221_hr_extend.parquet")

ReadDFParquet.printSchema()
ReadDFParquet.show(10,False)

# Cargar archivo CVS **** Debera ser el ORC NO EL CSV *****

ReadDFCSV = spark.read.csv("C:/Users/joni_/Downloads/HR_Rawdata_Audiencia_20230201.csv", sep=',',
                         inferSchema=True, header=True)

ReadDFCSV.printSchema()











# Register the DataFrame as a SQL temporary view
ReadDFParquet.createOrReplaceTempView("View")