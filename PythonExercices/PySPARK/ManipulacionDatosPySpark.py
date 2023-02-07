# Crear SparkSession es el punto de entrada y conecta con el cluster de Spark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ManipulacionDatosPySpark").getOrCreate()

# Leer informacion de un Archivo
readDF = spark.read.load("C:/Users/joni_/Downloads/SSNMX_catalogo.csv",
                         format="csv", sep=",",
                         inferSchema="true",
                         header="true")

readDF.show()



