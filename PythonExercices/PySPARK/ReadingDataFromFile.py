# Cargar librera
from pyspark.sql import SparkSession
# Crear sesión
spark = SparkSession.builder.appName("Data_Wrangling").getOrCreate()

# Cargar el archivo
ReadDF = spark.read.load("C:/Users/joni_/Downloads/movie_data_tmbd.csv",
                         format="csv", sep="|",
                         inferSchema="true",
                         header="true")

# Register the DataFrame as a SQL temporary view
ReadDF.createOrReplaceTempView("View")

# Más que nada es como una consulta
QUERY = spark.sql("""
SELECT * 
FROM View
LIMIT 10
""")
#Imprimir el QUERY
# ---> QUERY.show()

# Imprimir el esquema en formato de arbol tenemos una visualización sobre el tipo
# ---> QUERY.printSchema()
# root
#  |-- adult: string (nullable = true)
#  |-- backdrop_path: string (nullable = true)
#  |-- belongs_to_collection: string (nullable = true)
#  |-- budget: string (nullable = true)
#  |-- genres: string (nullable = true)
#  |-- homepage: string (nullable = true)
#  |-- id: integer (nullable = true)
#  |-- imdb_id: string (nullable = true)
#  |-- original_language: string (nullable = true)
#  |-- original_title: string (nullable = true)
#  |-- overview: string (nullable = true)
#  |-- popularity: string (nullable = true)
#  |-- poster_path: string (nullable = true)
#  |-- production_companies: string (nullable = true)
#  |-- production_countries: string (nullable = true)
#  |-- release_date: string (nullable = true)
#  |-- revenue: string (nullable = true)
#  |-- runtime: string (nullable = true)
#  |-- spoken_languages: string (nullable = true)
#  |-- status: string (nullable = true)
#  |-- tagline: string (nullable = true)
#  |-- title: string (nullable = true)
#  |-- video: string (nullable = true)
#  |-- vote_average: string (nullable = true)
#  |-- vote_count: integer (nullable = true)
#  |-- cast: string (nullable = true)
#  |-- directors: string (nullable = true)

# ---> print("Total de registro en el DATASET: " + str(ReadDF.count()))
# Definamos una lista de las columnas que deseamos imprimir
select_columnas: list = ["id", "budget", "popularity", "release_date", "revenue", "title"]

# Subconjunto que requieren columnas del DATAFRAME
ReadDF = ReadDF.select(*select_columnas)
# ---> ReadDF.show()
# +-----+-------+------------------+------------+-------+--------------------+
# |   id| budget|        popularity|release_date|revenue|               title|
# +-----+-------+------------------+------------+-------+--------------------+
# |43000|      0|             3.892|  1962-05-23|      0|The Elusive Corporal|
# |43001|      0|             5.482|  1962-11-12|      0|  Sundays and Cybele|
# |43002|      0|             8.262|  1962-05-24|      0|Lonely Are the Brave|
# |43003|      0|              7.83|  1975-03-12|      0|          F for Fake|
# |43004| 500000|             5.694|  1962-10-09|      0|Long Day's Journe...|
# |43006|      0|             2.873|  1962-03-09|      0|           My Geisha|
# |43007|      0|             3.433|  1962-10-31|      0|Period of Adjustment|
# |43008|      0|             7.869|  1959-03-13|      0|    The Hanging Tree|
# |43010|      0|             3.775|  1962-01-01|      0|Sherlock Holmes a...|
# |43011|      0|             7.185|  1962-01-01|      0|  Sodom and Gomorrah|
# |43012|7000000|             8.193|  1962-11-21|4000000|         Taras Bulba|
# |43013|      0|             4.408|  1962-04-17|      0|The Counterfeit T...|
# |43014|      0|             5.562|  1962-10-24|      0|     Tower of London|
# |43015|      0|             3.083|  1962-12-07|      0|Varan the Unbelie...|
# |43016|      0|3.5060000000000002|  1962-04-12|      0|Waltz of the Tore...|
# |43017|      0|             3.926|  1961-10-11|      0|         Back Street|
# |43018|      0|             3.623|  1961-06-02|      0|Gidget Goes Hawaiian|
# |43019|      0|             2.112|  2010-05-28|      0|Schuks Tshabalala...|
# |43020|      0|             9.668|  1961-06-15|      0|The Colossus of R...|
# |43021|      0|             4.033|  2008-08-22|      0|          Sex Galaxy|
# +-----+-------+------------------+------------+-------+--------------------+
# only showing top 20 rows

# Podemos extender el número de rows que se despliegan por default
# ---> ReadDF.show(40,False)
# only showing top 40 rows

"""Valores Faltantes"""
# Podemos calcular valores faltantes en una columna o en multiples columnas
# usando funciones de construcción en PySpark
from pyspark.sql.functions import *

Missing_Values: int = ReadDF.filter((ReadDF['popularity']=='')|ReadDF['popularity'].isNull()|isnan(ReadDF['popularity'])).count()
print('\t' + str(Missing_Values))










