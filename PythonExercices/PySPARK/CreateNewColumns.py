# Cargar librera
from pyspark.sql import SparkSession
# Crear sesión
spark = SparkSession.builder.appName("Data_Wrangling").getOrCreate()
# El tipo de archivo PySpark puede leer otros formatos como: json, parquet, orc
# Cargar el archivo
ReadDF = spark.read.load("C:/Users/joni_/Downloads/movie_data_tmbd.csv",
                         format="csv", sep="|",
                         inferSchema="true",
                         header="true")


# Register the DataFrame as a SQL temporary view
ReadDF.createOrReplaceTempView("View")
# -----------------------------------------------------------------------------------------------#
# Definamos una lista de las columnas que deseamos imprimir
select_columnas: list = ["id", "budget", "popularity", "release_date", "revenue", "title"]
# Subconjunto que requieren columnas del DATAFRAME
ReadDF = ReadDF.select(*select_columnas)
# ---> ReadDF.show()
# -----------------------------------------------------------------------------------------------#

# Creando nuevas columnas
# Crear nuevas columnas juega un papel muy importante un muchas aplicaciones analíticas
# Spark ofrece multiples formas para crear nuevas columnas. El método más simple es:
# a traves de la función withColumn.
# Digamos que queremos calcular la varianza de la popularity
# La Varianza es la medida de que dispersos de la mediana está representada por la sig. Fórmula.

# Calculemos primero la media usando la función agg que es usada aquí para buscar cierta estadística
MeanPop = ReadDF.agg({'popularity':'mean'}).collect()[0]['avg(popularity)']
counts_obs = ReadDF.count()

# --> print(MeanPop) # 4.542358537469025
# --> print(counts_obs) # 120127

ConsultaMean = spark.sql ("""
SELECT AVG(popularity) AS mean_popularity
FROM View
""")
# --> ConsultaMean.show()
# +-----------------+
# |             Mean|
# +-----------------+
# |4.542358537469025|
# +-----------------+

# Como vemos con SQL Spark y SQL estandar podemos obtener el mismo resultado
# Agreguemos esto a todas las filas, ya que necesitamos este valor junto con el valor individual
# valores de observación
# La función lit en el camino para interactuar con las literales de las columnas
from pyspark.sql.functions import lit
ReadDF = ReadDF.withColumn('mean_popularity',lit(MeanPop))

# La columna mean_popularity es el mismo valor para todos los renglones
ReadDF = ReadDF.withColumn('varaiance', pow((ReadDF['popularity']-ReadDF['mean_popularity']),2))

# Este comando suma todas las diferencias a lo largo de los renglones
variance_sum = ReadDF.agg({'varaiance':'sum'}).collect()[0]['sum(varaiance)']

# El paso final, dividiremos la suma por el número de observaciones en la cual nos da el resultado
variance_population = (variance_sum/counts_obs-1)
print(variance_population) # 237.7144111833235

# Aunque el cálculo de la varianza involucra varios pasos, la idea es dar un panorama
# de las operaciones que puede hacer para crear nuevas caracteristicas.







