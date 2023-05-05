# Estos siguientes ejemplos se encuentran en el CAPÍTULO 3
# Conoceremos la utilidad de algunas funciones avanzadas disponibles en PySpark
# Nos enfocaremos en las funciones de ventana y otro topicos que son utiles
# en la creación y aplicación de programas de SPARK de grandes sets de datos.
# Se introducen los temas de visualización y procesos de ML.

# * Manipulaciones adicionales
# * Visualizaciones de los datos
# * Introducción a ML



# Cargar librera
import pyspark.sql.dataframe
from pyspark.sql import SparkSession
from pyspark.sql.functions import *

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

# Definamos una lista de las columnas que deseamos imprimir
select_columnas: list = ["id", "budget", "popularity", "release_date", "revenue", "title"]

# Subconjunto que requieren columnas del DATAFRAME
ReadDF = ReadDF.select(*select_columnas)
# --> ReadDF.show(10,False)


# Funciones de String

df_with_newcols : pyspark.sql.dataframe.DataFrame = ReadDF.select('id','budget','popularity'). \
    withColumn('budget_cat', when(ReadDF['budget']<10000000,'Small').
               when(ReadDF['budget']<100000000,'Medium').
               otherwise('Big')).withColumn('ratings', when(ReadDF['popularity']<3,'Low').
                                            when(ReadDF['popularity']<5,'Mid').otherwise('High'))
# Ver el DataFrame df_with_newcols
# --> df_with_newcols.show(15, False)
# +-----+-------+------------------+----------+-------+
# |id   |budget |popularity        |budget_cat|ratings|
# +-----+-------+------------------+----------+-------+
# |43000|0      |3.892             |Small     |Mid    |
# |43001|0      |5.482             |Small     |High   |
# |43002|0      |8.262             |Small     |High   |
# |43003|0      |7.83              |Small     |High   |
# |43004|500000 |5.694             |Small     |High   |
# |43006|0      |2.873             |Small     |Low    |
# |43007|0      |3.433             |Small     |Mid    |
# |43008|0      |7.869             |Small     |High   |
# |43010|0      |3.775             |Small     |Mid    |
# |43011|0      |7.185             |Small     |High   |
# |43012|7000000|8.193             |Small     |High   |
# |43013|0      |4.408             |Small     |Mid    |
# |43014|0      |5.562             |Small     |High   |
# |43015|0      |3.083             |Small     |Mid    |
# |43016|0      |3.5060000000000002|Small     |Mid    |
# +-----+-------+------------------+----------+-------+
# only showing top 15 rows

# SI queremos concatenar los valores de la columna budget_cat y ratings en una sola
# columna, lo podemos hacer con la función 'concat'
# Como primer paso, cambiemos el caso de la nueva columna a lowercase y trim removiendo
# espacios en blanco usando las funciones trim y lower.

# Concatenado dos variables
df_with_newcols = df_with_newcols.withColumn('BudgetRating_Category',concat(df_with_newcols.budget_cat,df_with_newcols.ratings))

# Cambiando la variable
df_with_newcols = df_with_newcols.withColumn('BudgetRating_Category',trim(lower(df_with_newcols.BudgetRating_Category)))
# --> df_with_newcols.show(10,False)

# +-----+------+----------+----------+-------+---------------------+
# |id   |budget|popularity|budget_cat|ratings|BudgetRating_Category|
# +-----+------+----------+----------+-------+---------------------+
# |43000|0     |3.892     |Small     |Mid    |smallmid             |
# |43001|0     |5.482     |Small     |High   |smallhigh            |
# |43002|0     |8.262     |Small     |High   |smallhigh            |
# |43003|0     |7.83      |Small     |High   |smallhigh            |
# |43004|500000|5.694     |Small     |High   |smallhigh            |
# |43006|0     |2.873     |Small     |Low    |smalllow             |
# |43007|0     |3.433     |Small     |Mid    |smallmid             |
# |43008|0     |7.869     |Small     |High   |smallhigh            |
# |43010|0     |3.775     |Small     |Mid    |smallmid             |
# |43011|0     |7.185     |Small     |High   |smallhigh            |
# +-----+------+----------+----------+-------+---------------------+
# only showing top 10 rows

# Registrar un tabla temporal

df_with_newcols.registerTempTable('OneUse')
consulta = spark.sql("""
SELECT ratings, COUNT(ratings)
FROM OneUse
GROUP BY ratings""")

# --> df_with_newcols.show()
# +-------+--------------+
# |ratings|count(ratings)|
# +-------+--------------+
# |   High|         28451|
# |    Low|         71878|
# |    Mid|         19798|
# +-------+--------------+

# Funciones de Ventana / Window Functions
# Importar las librerias para las funciones de ventana

from pyspark.sql.window import *

# Step 1: Filtra los valores faltantes
df_with_newcols = df_with_newcols.filter((df_with_newcols['popularity'].isNotNull()) & (~isnan(df_with_newcols['popularity'])))
# df_with_newcols.show(10,False)
# +-----+------+----------+----------+-------+---------------------+
# |id   |budget|popularity|budget_cat|ratings|BudgetRating_Category|
# +-----+------+----------+----------+-------+---------------------+
# |43000|0     |3.892     |Small     |Mid    |smallmid             |
# |43001|0     |5.482     |Small     |High   |smallhigh            |
# |43002|0     |8.262     |Small     |High   |smallhigh            |
# |43003|0     |7.83      |Small     |High   |smallhigh            |
# |43004|500000|5.694     |Small     |High   |smallhigh            |
# |43006|0     |2.873     |Small     |Low    |smalllow             |
# |43007|0     |3.433     |Small     |Mid    |smallmid             |
# |43008|0     |7.869     |Small     |High   |smallhigh            |
# |43010|0     |3.775     |Small     |Mid    |smallmid             |
# |43011|0     |7.185     |Small     |High   |smallhigh            |
# +-----+------+----------+----------+-------+---------------------+
# only showing top 10 rows

# Como poner la linea anterior en comando SQL la cual discrimina los valores nulos
consulta_filter = spark.sql("""
SELECT *
FROM OneUse
WHERE popularity IS NOT NULL""")
# consulta_filter.show()


# Primero quise saber cuantos registros Nulos existen en el DF Usando una consulta SQL
# Esto es con la vista de la tabla anterior lo que signfica que aún no se discriminan los NULOS
consulta_num_nulos = spark.sql("""
SELECT COUNT(*) AS Num_Nulos
FROM OneUse 
WHERE popularity IS NULL""")
# --> consulta_num_nulos.show()

# +---------+
# |Num_Nulos|
# +---------+
# |     1059|
# +---------+

# Tuve que hacer otra vista temporal de la tabla porque se aplicaron los filtros y en esta nueva vista vemos
# que en el resultado salen 0 nulos que ya fueron discriminados
df_with_newcols.registerTempTable('TwoUse')

after_filter_nulos = spark.sql("""
SELECT COUNT(*) AS Num_Nulos
FROM TwoUse
WHERE popularity IS NULL""")
# --> after_filter_nulos.show()

# +---------+
# |Num_Nulos|
# +---------+
# |        0|
# +---------+

