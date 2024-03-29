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

Missing_Values = ReadDF.filter((ReadDF['popularity']=='') | ReadDF['popularity'].isNull() | isnan(ReadDF['popularity'])).count()
# print("Valores faltantes: " + str(Missing_Values))
# Valores faltantes: 1059

# Si necesitas calcular todos los valores faltantes en el  DATAFRAME puedes usar el sig. Comando
CommandMissingValues = ReadDF.select([count(when((col(c)=='') | col(c).isNull() | isnan(c), c)).
                                 alias(c) for c in ReadDF.columns])
# ---> CommandMissingValues.show()
# +---+------+----------+------------+-------+-----+
# | id|budget|popularity|release_date|revenue|title|
# +---+------+----------+------------+-------+-----+
# |658|   658|      1059|        1487|   1059| 1455|
# +---+------+----------+------------+-------+-----+


"""Calcular Frecuencias"""
# Calculemos las frecuencias de variables categorical
# Glosario: Las variables categoricas son variables tipo STRING que existen en un DATASET
# Primero verifiquemos si hay algún título repetido en el DATASET:

TitulosRepetidos = ReadDF.groupby(ReadDF['title']).count()
# ---> TitulosRepetidos.show()

QUERYTWO = spark.sql("""
SELECT title, COUNT(title)
FROM View
GROUP BY title
""")
# ---> QUERYTWO.show()

# ¡¡Ambos comando devuelven lo mismo. Uno es con comandos nativos de PySpark y el segundo con comandos de SQL!!

# +--------------------+-----+
# |               title|count|
# +--------------------+-----+
# |   The Corn Is Green|    2|
# |Meet The Browns -...|    1|
# |Morenita, El Esca...|    1|
# | Father Takes a Wife|    1|
# |    Taking The Curve|    1|
# |           Fleshburn|    1|
# |          Dead Lenny|    1|
# |El juego de la silla|    1|
# |              Sargad|    1|
# |                 Kin|    3|
# |I Don't Feel at H...|    1|
# |Penguins of Madag...|    1|
# | Ormayundo Ee Mukham|    1|
# |         Eat With Me|    1|
# |  Ainda Há Pastores?|    1|
# |The Werewolf of W...|    1|
# |    Conquering China|    1|
# |Discovering the R...|    1|
# |My Wife Is a Gang...|    1|
# |Depeche Mode: Tou...|    1|
# +--------------------+-----+
# only showing top 20 rows
# Figura 2-6 Output of one_way frequency

# El comando anterior devuelve el número de veces que aparece un título en el DATASET
# A menudo tu queras observar los datos ordenados

TitulosRepetidosOrdenados = ReadDF.groupby(ReadDF['title']).count().sort(desc('count'))
# ---> TitulosRepetidosOrdenados.show(10,False)

# +--------------------+-----+
# |title               |count|
# +--------------------+-----+
# |null                |1455 |
# |Mother              |14   |
# |The Intruder        |13   |
# |Macbeth             |13   |
# |Treasure Island     |13   |
# |The Three Musketeers|12   |
# |Cinderella          |12   |
# |Alone               |12   |
# |Desire              |12   |
# |First Love          |12   |
# +--------------------+-----+
# only showing top 10 rows
# Figura 2-7 Output of one_way frequency sorted

"""Ordenamiento y filtrado 'Un camino de Frecuencias'"""
# Primero filtremos los valores que no son NULL. Nosotros usaremos el sifgi !=
# para crear un DATASET temporal, el cual está hecho intensionalmente para demostrar
# el uso de la condición NOT.

# Subconjunto y Creando un DATAFRAME TEMPORAL para eliminar cualquier valor faltante
ReadDF_Temp = ReadDF.filter((ReadDF['title']!='') & (ReadDF['title'].isNotNull()) & (~isnan(ReadDF['title'])))

# Subconjunto el DATAFRAME a títulos que están repetidos más de cuatro veces.
Filtro_uno = ReadDF_Temp.groupby(ReadDF_Temp['title']).count().filter("`count` >4").sort(col("count").desc())
# ---> Filtro_uno.show(10, False)

# +--------------------+-----+
# |title               |count|
# +--------------------+-----+
# |Mother              |14   |
# |The Intruder        |13   |
# |Macbeth             |13   |
# |Treasure Island     |13   |
# |First Love          |12   |
# |Alone               |12   |
# |Desire              |12   |
# |Cinderella          |12   |
# |The Three Musketeers|12   |
# |Love                |11   |
# +--------------------+-----+
# only showing top 10 rows
# Figure 2-8 Output of filtered and sorted version of one-way frequency

# El siguiente comando es para encontrar el número de títulos que están repetidos cuatro veces o más.
Filtro_dos = ReadDF_Temp.groupby(ReadDF_Temp['title']).count().filter("`count` >=4").sort(col("count").desc()).count()
# ---> print ("Output: \n" + str(Filtro_dos))

# El siguiente comando es para eliminar el DATAFRAME TEMPORAL que se creo en el proceso.

del ReadDF_Temp

"""Casting de variables 20-02-2023"""
# Algunas operaciones pueden tener resultados incorrectos si los tipos de datos
# no están correctamente identificados. Es altamente recomendable identificar de primera mano
# el tipo de dato para cualquiera de nuestros analísis. Ahora veremos como hacer un cast de algunas variables
# para tener los tipos correctos en nuestra DATA.

#Antes de casting
# ---> print(ReadDF.dtypes)
# [('id', 'int'), ('budget', 'string'), ('popularity', 'string'), ('release_date', 'string'), ('revenue', 'string'), ('title', 'string')]
# Con el comando de dtypes podemos ver el tipo de dato que esta asociado a la columna y claramente algunos están equivocados particularmente la fecha


# Despues del Casting
ReadDF = ReadDF.withColumn('budget',ReadDF['budget'].cast('float'))
# ---> print(ReadDF.dtypes)
# [('id', 'int'), ('budget', 'float'), ('popularity', 'string'), ('release_date', 'string'), ('revenue', 'string'), ('title', 'string')]
# Figure 2.6 Datatypes after casting
# Vemos que la columna 'budget' cambio a tipo float
# Observamos que usamos la función cast. También deberás haber notado que usamos una función adicional
# llamada .withColumn que es muy conocida en Pyspark. Es utilizada para actualizar los valores
# renombrar y convertir datatypes y para crear nuevas columnas.

# Identificar y asignar la lista de variables
int_vars: list = ['id']
float_vars: list = ['budget', 'popularity', 'revenue']
date_vars:list = ['release_date']

# Convirtiendo las variables
for column in int_vars:
    ReadDF=ReadDF.withColumn(column,ReadDF[column].cast(IntegerType()))
for column in float_vars:
    ReadDF=ReadDF.withColumn(column,ReadDF[column].cast(FloatType()))
for column in date_vars:
    ReadDF=ReadDF.withColumn(column,ReadDF[column].cast(DateType()))

# -> print(ReadDF.dtypes)
# [('id', 'int'), ('budget', 'float'), ('popularity', 'float'), ('release_date', 'date'), ('revenue', 'float'), ('title', 'string')]
# Se cambiaron correctamente los tipos de datos en el DATAFRAME

# -> ReadDF.show(10,False)
# +-----+--------+----------+------------+-------+---------------------------------------+
# |id   |budget  |popularity|release_date|revenue|title                                  |
# +-----+--------+----------+------------+-------+---------------------------------------+
# |43000|0.0     |3.892     |1962-05-23  |0.0    |The Elusive Corporal                   |
# |43001|0.0     |5.482     |1962-11-12  |0.0    |Sundays and Cybele                     |
# |43002|0.0     |8.262     |1962-05-24  |0.0    |Lonely Are the Brave                   |
# |43003|0.0     |7.83      |1975-03-12  |0.0    |F for Fake                             |
# |43004|500000.0|5.694     |1962-10-09  |0.0    |Long Day's Journey Into Night          |
# |43006|0.0     |2.873     |1962-03-09  |0.0    |My Geisha                              |
# |43007|0.0     |3.433     |1962-10-31  |0.0    |Period of Adjustment                   |
# |43008|0.0     |7.869     |1959-03-13  |0.0    |The Hanging Tree                       |
# |43010|0.0     |3.775     |1962-01-01  |0.0    |Sherlock Holmes and the Deadly Necklace|
# |43011|0.0     |7.185     |1962-01-01  |0.0    |Sodom and Gomorrah                     |
# +-----+--------+----------+------------+-------+---------------------------------------+
# only showing top 10 rows
# Figure 2-12 Glimpse of data after changing the datatype

"""Estadística Descriptiva"""
# Para analizar cualquier tipo de data, deberíamos estar interesados en cualquier
# tipo de información como su distribución y dispersión.
# Spark tiene a un repositorio de funciones que pueden hacerte calcular fácilmente estos campos.
# La función describe en Spark es muy útil nos puede proporcionar la cuenta de los totales de valores
# no faltantes por cada columna, mediana, promedio, desviación estandar y valores minimos y maximos.


# -> ReadDF.describe().show()
# +-------+------------------+--------------------+------------------+--------------------+--------------------+
# |summary|                id|              budget|        popularity|             revenue|               title|
# +-------+------------------+--------------------+------------------+--------------------+--------------------+
# |  count|            119469|              119073|            118671|              118671|              118672|
# |   mean|236930.37953778805|    1935164.88358402| 4.542358538121745|  5177548.7368185995|            Infinity|
# | stddev| 883010.9925616537|1.1924348980601171E7|15.544944047515473|4.5767315120673515E7|                 NaN|
# |    min|                 0|                 0.0|               0.6|                 0.0|!Women Art Revolu...|
# |    max|         215880014|               3.8E8|          2068.491|        2.79780045E9|   ＡLife That Sings|
# +-------+------------------+--------------------+------------------+--------------------+--------------------+


# Valores desconocidos en la columna de budget estas marcadas en 0, filtremos fuera estos valores
# antes de calcular la mediana.

ReadDF_Temp = ReadDF.filter((ReadDF['budget'] != 0) & (ReadDF['budget'].isNotNull()) &
                    (~isnan(ReadDF['budget'])))

# El segundo parametro indica el valor medio, el cual es 0.5 tu puedes tratar de ajustar
# el valor para calcular otros percentiles.

median = ReadDF.approxQuantile('budget',[0.5],0.1)
# -> print ('El valor medio de budget es: ' + str (median))


"""Unicos/Valores Diferentes Y Conteos"""

# Tú en ciertas ocasiones queras solo saber el número de niveles o cardinalidad con una variable
# Para hacer esto podemos usar la función countDistinct disponible en Spark


# Cuenta los valores diferentes para los titulo
Contador = ReadDF.agg(countDistinct(col('title')).alias('count'))
# -> Contador.show()
# +------+
# | count|
# +------+
# |107973|
# +------+
# Figure 2-14 Distinct titles count output
# Algo interesante de la anterior consulta es que utiliza la método Aggregate on the entire DataFrame without groups (shorthand for df.groupBy().agg()).

Consulta = spark.sql("""
SELECT 
COUNT(DISTINCT(title)) AS count
FROM View
""")
# -> Consulta.show()
# +---------------------+
# |count(DISTINCT title)|
# +---------------------+
# |               107973|
# +---------------------+


# Contar cuantas diferentes ocurrencias de títulos existen SPARK-SQL
TitulosDiff = ReadDF.select('title').distinct()
# --> TitulosDiff.show(10,False)

# +--------------------------+
# |title                     |
# +--------------------------+
# |The Corn Is Green         |
# |Meet The Browns - The Play|
# |Morenita, El Escandalo    |
# |Father Takes a Wife       |
# |Taking The Curve          |
# |Fleshburn                 |
# |Dead Lenny                |
# |El juego de la silla      |
# |Sargad                    |
# |Kin                       |
# +--------------------------+
# only showing top 10 rows
# Figure. 2-15 Distinct titles output

# Ahora con SQL
Consulta_TITULOS = spark.sql ("""
SELECT DISTINCT(title)
FROM View
""")
# --> Consulta_TITULOS.show(10,False)

# Extrae el año por fecha de lanzamiento
# Haremos un DF temporal para esto

DFTEMP_YearRelease = ReadDF.withColumn('release_year', year('release_date'))
# --> DFTEMP_YearRelease.show(10,False)

# +-----+--------+----------+------------+-------+---------------------------------------+------------+
# |id   |budget  |popularity|release_date|revenue|title                                  |release_year|
# +-----+--------+----------+------------+-------+---------------------------------------+------------+
# |43000|0.0     |3.892     |1962-05-23  |0.0    |The Elusive Corporal                   |1962        |
# |43001|0.0     |5.482     |1962-11-12  |0.0    |Sundays and Cybele                     |1962        |
# |43002|0.0     |8.262     |1962-05-24  |0.0    |Lonely Are the Brave                   |1962        |
# |43003|0.0     |7.83      |1975-03-12  |0.0    |F for Fake                             |1975        |
# |43004|500000.0|5.694     |1962-10-09  |0.0    |Long Day's Journey Into Night          |1962        |
# |43006|0.0     |2.873     |1962-03-09  |0.0    |My Geisha                              |1962        |
# |43007|0.0     |3.433     |1962-10-31  |0.0    |Period of Adjustment                   |1962        |
# |43008|0.0     |7.869     |1959-03-13  |0.0    |The Hanging Tree                       |1959        |
# |43010|0.0     |3.775     |1962-01-01  |0.0    |Sherlock Holmes and the Deadly Necklace|1962        |
# |43011|0.0     |7.185     |1962-01-01  |0.0    |Sodom and Gomorrah                     |1962        |
# +-----+--------+----------+------------+-------+---------------------------------------+------------+
# only showing top 10 rows
# Extraer el año de la columna release_date y guardarla en una nueva columna y esto almacenarlo un un DF Temporal

# CONSULTA EN SQL COMÚN
TEMP_YearRelease_SQL = spark.sql("""
SELECT id, budget,popularity, release_date, revenue, title, YEAR(release_date) AS release_year
FROM View
""")
# --> TEMP_YearRelease_SQL.show(10,False)

# Como vemos tenemos el mismo resultado con un Query en SQL
# +-----+------+----------+------------+-------+---------------------------------------+------------+
# |id   |budget|popularity|release_date|revenue|title                                  |release_year|
# +-----+------+----------+------------+-------+---------------------------------------+------------+
# |43000|0     |3.892     |1962-05-23  |0      |The Elusive Corporal                   |1962        |
# |43001|0     |5.482     |1962-11-12  |0      |Sundays and Cybele                     |1962        |
# |43002|0     |8.262     |1962-05-24  |0      |Lonely Are the Brave                   |1962        |
# |43003|0     |7.83      |1975-03-12  |0      |F for Fake                             |1975        |
# |43004|500000|5.694     |1962-10-09  |0      |Long Day's Journey Into Night          |1962        |
# |43006|0     |2.873     |1962-03-09  |0      |My Geisha                              |1962        |
# |43007|0     |3.433     |1962-10-31  |0      |Period of Adjustment                   |1962        |
# |43008|0     |7.869     |1959-03-13  |0      |The Hanging Tree                       |1959        |
# |43010|0     |3.775     |1962-01-01  |0      |Sherlock Holmes and the Deadly Necklace|1962        |
# |43011|0     |7.185     |1962-01-01  |0      |Sodom and Gomorrah                     |1962        |
# +-----+------+----------+------------+-------+---------------------------------------+------------+
# only showing top 10 rows

# Ahora extraigamos el MES, que es muy similar al año
DFTEMP_MonthRelease = ReadDF.withColumn('release_month',month('release_date'))
# -> DFTEMP_MonthRelease.show(10,False)

# +-----+--------+----------+------------+-------+---------------------------------------+-------------+
# |id   |budget  |popularity|release_date|revenue|title                                  |release_month|
# +-----+--------+----------+------------+-------+---------------------------------------+-------------+
# |43000|0.0     |3.892     |1962-05-23  |0.0    |The Elusive Corporal                   |5            |
# |43001|0.0     |5.482     |1962-11-12  |0.0    |Sundays and Cybele                     |11           |
# |43002|0.0     |8.262     |1962-05-24  |0.0    |Lonely Are the Brave                   |5            |
# |43003|0.0     |7.83      |1975-03-12  |0.0    |F for Fake                             |3            |
# |43004|500000.0|5.694     |1962-10-09  |0.0    |Long Day's Journey Into Night          |10           |
# |43006|0.0     |2.873     |1962-03-09  |0.0    |My Geisha                              |3            |
# |43007|0.0     |3.433     |1962-10-31  |0.0    |Period of Adjustment                   |10           |
# |43008|0.0     |7.869     |1959-03-13  |0.0    |The Hanging Tree                       |3            |
# |43010|0.0     |3.775     |1962-01-01  |0.0    |Sherlock Holmes and the Deadly Necklace|1            |
# |43011|0.0     |7.185     |1962-01-01  |0.0    |Sodom and Gomorrah                     |1            |
# +-----+--------+----------+------------+-------+---------------------------------------+-------------+
# only showing top 10 rows

# Ahora extraigamos el MES, que es muy similar al año
DFTEMP_DayRelease = ReadDF.withColumn('release_day', dayofmonth('release_date'))
# --> DFTEMP_DayRelease.show(10,False)
# +-----+--------+----------+------------+-------+---------------------------------------+-----------+
# |id   |budget  |popularity|release_date|revenue|title                                  |release_day|
# +-----+--------+----------+------------+-------+---------------------------------------+-----------+
# |43000|0.0     |3.892     |1962-05-23  |0.0    |The Elusive Corporal                   |23         |
# |43001|0.0     |5.482     |1962-11-12  |0.0    |Sundays and Cybele                     |12         |
# |43002|0.0     |8.262     |1962-05-24  |0.0    |Lonely Are the Brave                   |24         |
# |43003|0.0     |7.83      |1975-03-12  |0.0    |F for Fake                             |12         |
# |43004|500000.0|5.694     |1962-10-09  |0.0    |Long Day's Journey Into Night          |9          |
# |43006|0.0     |2.873     |1962-03-09  |0.0    |My Geisha                              |9          |
# |43007|0.0     |3.433     |1962-10-31  |0.0    |Period of Adjustment                   |31         |
# |43008|0.0     |7.869     |1959-03-13  |0.0    |The Hanging Tree                       |13         |
# |43010|0.0     |3.775     |1962-01-01  |0.0    |Sherlock Holmes and the Deadly Necklace|1          |
# |43011|0.0     |7.185     |1962-01-01  |0.0    |Sodom and Gomorrah                     |1          |
# +-----+--------+----------+------------+-------+---------------------------------------+-----------+
# only showing top 10 rows

# Calculando cuantos diferentes titulos hay por año
# Se tiene que usar el DATAFRAME temporal donde se extrajo el año en una nueva columna y despues se toma es columna para agrupar
DistinctTitles = DFTEMP_YearRelease.groupBy('release_year').agg(countDistinct('title'))
# --> DistinctTitles.show(10,False)
# +------------+------------+
# |release_year|count(title)|
# +------------+------------+
# |1959        |582         |
# |1990        |1027        |
# |1975        |797         |
# |1977        |892         |
# |1924        |53          |
# |2003        |1873        |
# |2007        |2763        |
# |2018        |5523        |
# |1974        |942         |
# |2015        |4415        |
# +------------+------------+
# only showing top 10 rows
# Figure 2-16 Distinct titles count by year

DFTEMP_YearRelease.createOrReplaceTempView("Temporal")
YearDiff = spark.sql("""
SELECT release_year, COUNT(DISTINCT(title))
FROM Temporal
GROUP BY release_year
""")

# --> YearDiff.show(10,False)
# +------------+---------------------+
# |release_year|count(DISTINCT title)|
# +------------+---------------------+
# |1959        |582                  |
# |1990        |1027                 |
# |1975        |797                  |
# |1977        |892                  |
# |1924        |53                   |
# |2003        |1873                 |
# |2007        |2763                 |
# |2018        |5523                 |
# |1974        |942                  |
# |2015        |4415                 |
# +------------+---------------------+
# only showing top 10 rows



# Terminar la sesión de Spark
spark.stop()




