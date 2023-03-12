# Script que permite cargar un archivo csv con información de sismos con la cual se puede interactuar y analizar

# Crear SparkSession es el punto de entrada y conecta con el cluster de Spark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ManipulacionDatosPySpark").getOrCreate()

# Leer información de un Archivo de información de sismos en México
ReadDF = spark.read.load("C:/Users/joni_/Downloads/SSNMX_catalogo.csv",
                         format="csv", sep=",",
                         inferSchema="true",
                         header="true")

# readDF.show()

# Print the schema in a tree format tenemos una visualización sobre el tipo
# readDF.printSchema()

# Register the DataFrame as a SQL temporary view
ReadDF.createOrReplaceTempView("Sismos")

#Vista Global Temporal
ReadDF.createGlobalTempView("Global")

# Un query donde me trae 10 elementos al azar de la tabla
QuerySismos = spark.sql(""" 
    SELECT *
    FROM Sismos
    LIMIT 10
    """)
# QuerySismos.show()

# Creemos un query donde por fecha me diga cuantos sismos en un rango de cierta magnitud sucedieron
MgCinco = spark.sql ("""
SELECT Fecha, Magnitud, COUNT(Magnitud) AS NumSismos
FROM Sismos 
WHERE Magnitud BETWEEN 3 AND 5
GROUP BY Fecha, Magnitud
""")

# MgCinco.show()

# print(ReadDF.columns) # Encabezados del DataFrame
# ['Fecha', 'Hora', 'Magnitud', 'Latitud', 'Longitud', 'Profundidad', 'Referencia de localizacion', 'Fecha UTC', 'Hora UTC', 'Estatus']

# Hagamos un query donde nos devuelva los sismos con mayor magnitud por fecha y ordenarmos de mayor a menor
MagMaxSismos = spark.sql("""
SELECT Fecha, MAX(Magnitud) as MagnitudMaxima
FROM Sismos
GROUP BY Fecha, Magnitud
ORDER BY Magnitud DESC
""")

# MagMaxSismos.show()
# +---------+--------------+
# |Fecha UTC|MagnitudMaxima|
# +---------+--------------+
# |Fecha UTC|2.4           |
# |Fecha UTC|3.5           |
# |Fecha UTC|2.9           |
# |Fecha UTC|3.7           |
# |Fecha UTC|1.7           |
# +---------+--------------+
# only showing top 5 rows

# Ahora diagamos que queremos los top 10 sismos que reporto a mayor profundidad
# Lo agrupe por fecha porque por dia ocurrieron muchos sismos y solo me develve el mayor por dia
BigDepth = spark.sql("""
SELECT MAX(Profundidad) AS BigDepth_km, Fecha
FROM Sismos
GROUP BY Fecha
""")

BigDepth.show()
# +-----------+----------+
# |BigDepth_km|     Fecha|
# +-----------+----------+
# |      166.0|02/12/2022|
# |      237.0|03/12/2022|
# |      161.0|04/12/2022|
# |      179.0|06/12/2022|
# |      129.0|05/12/2022|
# |      140.0|07/12/2022|
# |      150.0|01/12/2022|
# +-----------+----------+


