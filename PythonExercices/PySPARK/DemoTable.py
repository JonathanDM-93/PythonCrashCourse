# Cargar librera
from pyspark.sql import SparkSession



# Crear sesión
spark = SparkSession.builder.appName("DemoTable").getOrCreate()


# El tipo de archivo PySpark puede leer otros formatos como: json, parquet, orc
# Cargar el archivo
ReadDF = spark.read.load("C:/Users/joni_/Downloads/TablaDemo.csv", # Ruta del Archivo
                         format="csv", sep=",",
                         inferSchema="true", # Inferir los typos de datos de las columnas
                         header="true") # Indicar que el archivo tiene encabezados

# --> ReadDF.printSchema()
# Vemos que si dedujo correctamente los tipos de dato de las columnas
#  |-- Nombre: string (nullable = true)
#  |-- Apellido: string (nullable = true)
#  |-- Edad: integer (nullable = true)

# --> ReadDF.show()
# +--------+---------+----+
# |  Nombre| Apellido|Edad|
# +--------+---------+----+
# |Jonathan|Maldonado|  29|
# |    Gina|   Juarez|  28|
# |   Karen|     Diaz|  15|
# |  Monica|      Rio|  35|
# |  Miguel|     Rosa|  20|
# +--------+---------+----+

# Ahora lo que haremos es hacer un query agregando un dato nuevo
ReadDF.createOrReplaceTempView("View")

# Aplicando consulta con comandos nativos de SPARK
filtered_df = ReadDF.select("Nombre", "Apellido", "Edad")

Query = spark.sql(""" 
SELECT *
FROM View
""")

# --> Query.show()

# +--------+---------+----+
# |  Nombre| Apellido|Edad|
# +--------+---------+----+
# |Jonathan|Maldonado|  29|
# |    Gina|   Juarez|  28|
# |   Karen|     Diaz|  15|
# |  Monica|      Rio|  35|
# |  Miguel|     Rosa|  20|
# +--------+---------+----+






# Elimar la vista temporal para ejecutar consultas con SQL estandar
spark.catalog.dropTempView("View")

# Terminar la sesión de Spark
spark.stop()