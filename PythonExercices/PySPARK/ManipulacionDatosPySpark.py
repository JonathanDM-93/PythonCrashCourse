# Crear SparkSession es el punto de entrada y conecta con el cluster de Spark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ManipulacionDatosPySpark").getOrCreate()

# Leer informacion de un Archivo
readDF = spark.read.load("C:/Users/joni_/Downloads/SSNMX_catalogo.csv",
                         format="csv", sep=",",
                         inferSchema="true",
                         header="true")

# readDF.show()

# Print the schema in a tree format tenemos una visualización sobre el tipo
# readDF.printSchema()

# Register the DataFrame as a SQL temporary view
readDF.createOrReplaceTempView("Sismos")

#Vista Global Temporal
readDF.createGlobalTempView("Global")

# Un query donde me trae 10 elementos de la tabla
QuerySismos = spark.sql(""" 
    SELECT *
    FROM Sismos
    LIMIT 10
    """)
QuerySismos.show()

# Creemos un query donde por fecha me diga cuantos sismos en un rango de cierta magnitud sucedieron
MgCinco = spark.sql ("""
SELECT Fecha, Magnitud, COUNT(Magnitud) AS NumSismos
FROM Sismos 
WHERE Magnitud BETWEEN 3 AND 5
GROUP BY Fecha, Magnitud
""")

MgCinco.show()