# Cargar librera
from pyspark.sql import SparkSession
# Crear sesión
spark = SparkSession.builder.appName("Data_Wrangling").getOrCreate()

# Importar librerias necesarias para el Cast
from pyspark.sql.types import *

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


"""Filtros/Filtrando"""
# Spark ofrece varias formas de filtrar los datos. Anteriormente, utilizamos la
# función filter(). Esto demuestra que tan importante es esta función a menudo
# en operaciones básicas.
# Tú también puedes encontrar la función where() para filtrar. Ambas funciones funcionan
# de la misma manera. Sin embargo, la función filter() es el estandar en Scala para esta función.
# .where() = .filter()

# El siguiente ejemplo se aplica la función .filter para filtrar los títulos que comiencen
# con las letras "Meet"

FilterTitles = ReadDF.filter(ReadDF['title'].like('Meet%'))
FilterTitles.show(10,False)
# Se observa que ahora solo devuelve los libros que inician con la palabra clave "Meet"
# +------+--------+----------+------------+-----------+--------------------------------+
# |id    |budget  |popularity|release_date|revenue    |title                           |
# +------+--------+----------+------------+-----------+--------------------------------+
# |43957 |500000.0|3.004     |2005-06-28  |1000000.0  |Meet The Browns - The Play      |
# |355515|0.0     |0.6       |1953-01-01  |0.0        |Meet Me at the Fair             |
# |279542|0.0     |0.764     |1978-07-01  |0.0        |Meeting in July                 |
# |39997 |0.0     |3.805     |1989-11-15  |0.0        |Meet the Hollowheads            |
# |131504|0.0     |1.259     |1956-03-09  |0.0        |Meet Me in Las Vegas            |
# |386882|0.0     |2.373     |1996-02-09  |0.0        |Meet Me in the Dream: Wonderland|
# |16710 |0.0     |8.892     |2008-03-21  |4.1939392E7|Meet the Browns                 |
# |20430 |0.0     |3.507     |2004-01-29  |0.0        |Meet Market                     |
# |271048|0.0     |0.624     |1937-06-04  |0.0        |Meet the Missus                 |
# |117825|0.0     |2.744     |1991-11-17  |0.0        |Meeting Venus                   |
# +------+--------+----------+------------+-----------+--------------------------------+
# only showing top 10 rows
# Fig 2-17 Filtering matches using "like" expression

#