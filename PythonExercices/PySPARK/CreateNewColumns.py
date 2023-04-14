# Cargar librera
import pyspark.sql.dataframe
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
# Algunos comandos útiles para saber que encabezados contiene nuestro DataFrame
# -->print(ReadDF.columns) # ['id', 'budget', 'popularity', 'release_date', 'revenue', 'title']
# --> print(ReadDF.columns[0]) # id

indices = ReadDF.columns.index('id')
# --> print(indices) # 0
# --> print(ReadDF.first()) # Primera fila
# --> print(ReadDF.count()) # Número de filas de DF 120127

# Definamos una lista de las columnas que deseamos imprimir
select_columnas: list = ["id", "budget", "popularity", "release_date", "revenue", "title"]
# Subconjunto que requieren columnas del DATAFRAME
ReadDF = ReadDF.select(*select_columnas)
# --> ReadDF.show(2,False)
# +-----+------+----------+------------+-------+--------------------+
# |id   |budget|popularity|release_date|revenue|title               |
# +-----+------+----------+------------+-------+--------------------+
# |43000|0     |3.892     |1962-05-23  |0      |The Elusive Corporal|
# |43001|0     |5.482     |1962-11-12  |0      |Sundays and Cybele  |
# +-----+------+----------+------------+-------+--------------------+
# only showing top 2 rows
# Data Frame original
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
from pyspark.sql.functions import lit, when, col

# Se inserta el cálculo de la media aritmetica en la columna 'mean_popularity'
ReadDF = ReadDF.withColumn('mean_popularity',lit(MeanPop))
# --> ReadDF.show(2,False)
# +-----+------+----------+------------+-------+--------------------+-----------------+
# |id   |budget|popularity|release_date|revenue|title               |mean_popularity  |
# +-----+------+----------+------------+-------+--------------------+-----------------+
# |43000|0     |3.892     |1962-05-23  |0      |The Elusive Corporal|4.542358537469025|
# |43001|0     |5.482     |1962-11-12  |0      |Sundays and Cybele  |4.542358537469025|
# +-----+------+----------+------------+-------+--------------------+-----------------+
# only showing top 2 rows
# -----------------------------------------------------------------------------------------------#

# La columna mean_popularity es el mismo valor para todos los renglones
# Lo que describe la linea 76 es: de la resta de la columna 'popularity' entre 'mean_popularity' guardalo en el campo 'varaiance'
ReadDF = ReadDF.withColumn('varaiance', pow((ReadDF['popularity']-ReadDF['mean_popularity']),2))
# --> ReadDF.show(2,False)
# +-----+------+----------+------------+-------+--------------------+-----------------+-------------------+
# |id   |budget|popularity|release_date|revenue|title               |mean_popularity  |varaiance          |
# +-----+------+----------+------------+-------+--------------------+-----------------+-------------------+
# |43000|0     |3.892     |1962-05-23  |0      |The Elusive Corporal|4.542358537469025|0.42296622725884925|
# |43001|0     |5.482     |1962-11-12  |0      |Sundays and Cybele  |4.542358537469025|0.8829260781073501 |
# +-----+------+----------+------------+-------+--------------------+-----------------+-------------------+
# only showing top 2 rows
# -----------------------------------------------------------------------------------------------#

# Este comando suma todas las diferencias a lo largo de los renglones
variance_sum = ReadDF.agg({'varaiance':'sum'}).collect()[0]['sum(varaiance)']

# El paso final, dividiremos la suma por el número de observaciones en la cual nos da el resultado
variance_population = (variance_sum/counts_obs-1)
# --> print(variance_population) # 237.7144111833235

# Aunque el cálculo de la varianza involucra varios pasos, la idea es dar un panorama
# de las operaciones que puede hacer para crear nuevas caracteristicas.

# -> ReadDF.show(5,False)
# +-----+------+----------+------------+-------+-----------------------------+-----------------+-------------------+
# |id   |budget|popularity|release_date|revenue|title                        |mean_popularity  |varaiance          |
# +-----+------+----------+------------+-------+-----------------------------+-----------------+-------------------+
# |43000|0     |3.892     |1962-05-23  |0      |The Elusive Corporal         |4.542358537469025|0.42296622725884925|
# |43001|0     |5.482     |1962-11-12  |0      |Sundays and Cybele           |4.542358537469025|0.8829260781073501 |
# |43002|0     |8.262     |1962-05-24  |0      |Lonely Are the Brave         |4.542358537469025|13.835732609779575 |
# |43003|0     |7.83      |1975-03-12  |0      |F for Fake                   |4.542358537469025|10.80858638615281  |
# |43004|500000|5.694     |1962-10-09  |0      |Long Day's Journey Into Night|4.542358537469025|1.3262780582204832 |
# +-----+------+----------+------------+-------+-----------------------------+-----------------+-------------------+
# only showing top 5 rows


# Si tenemos muchas variables que crea, ¿Cómo puedo hacer esto de una vez y mantener estructurado?

# En la siguiente sección de código definiremos una función en Python
# Pasaremos dos variables dentro de una función y tomando como base el umbral
# tomamos la decisión en retornar nuevas variables, ambos serán string.

"""
def new_cols(budget,popularity):
    if budget < 10000000:
        budget_cat = 'Small'
    elif budget < 100000000:
        budget_cat='Medium'
    else:
        budget_cat='Big'
    if popularity < 3:
        ratings='Low' # Si es 0,1,2
    elif popularity < 5:
        ratings='Mid' # Si es 3,4
    else:
        ratings = 'High' # El resto de los números
    return budget_cat,ratings
"""

# Se usarán las llamadas UDF(User Defined Functions) las cuales son similares a
# los métodos de pandas .map() y .apply() de un DataFrame y serie de Pandas.
# En palabras simples UDF nos permite usar los valores de los renglones de un DataFrame
# como entrada y pueden mapearse dentro de un DataFrame completo. Un hecho importante
# es que aquí es donde deberás especificar el tipo de dato en la sálida. Desafortunadamente,
# no hay forma de evitar esto. Esto puede ser doloroso cuando tienes que escribir en multiples columnas.
# Discutiremos otro método más adelante.

# Observa que hemos creado un nuevo tipo de StructType que contiene a las nuevas variables
# Tenemos que definir explícitamente que tipo de datatype va a devolver

"""
from pyspark.sql.types import StructType, StructField, StringType

# Aplica la UDF en el DataFrame

udfB=udf(new_cols,StructType([StructField("budget_cat", StringType(),True),
                              StructField("ratings", StringType(), True)]))

# En el siguiente comando nosotros pasaremos UDF con las columnas de entrada:
# budget & popularity
temp_df = ReadDF.select('id','budget','popularity').withColumn("newcat",udfB("budget","popularity"))

# Desagrupe las columnas de tipo de estructura en columnas individuales y suelte el
# tipo de estructura

df_with_newcols = temp_df.select('id','budget','popularity','newcat').\
    withColumn('budget_cat', temp_df.newcat.getItem('budget_cat')).\
    withColumn('ratings', temp_df.newcat.getItem('ratings')).drop('newcat')

df_with_newcols.show(10,False)
"""

df_with_newcols : pyspark.sql.dataframe.DataFrame = ReadDF.select('id','budget','popularity').\
    withColumn('budget_cat', when(ReadDF['budget']<10000000,'Small').
               when(ReadDF['budget']<100000000,'Medium').
               otherwise('Big')).withColumn('ratings', when(ReadDF['popularity']<3,'Low').
                                            when(ReadDF['popularity']<5,'Mid').otherwise('High'))

# --> df_with_newcols.show(10,False)
# +-----+------+----------+----------+-------+
# |id   |budget|popularity|budget_cat|ratings|
# +-----+------+----------+----------+-------+
# |43000|0     |3.892     |Small     |Mid    |
# |43001|0     |5.482     |Small     |High   |
# |43002|0     |8.262     |Small     |High   |
# |43003|0     |7.83      |Small     |High   |
# |43004|500000|5.694     |Small     |High   |
# |43006|0     |2.873     |Small     |Low    |
# |43007|0     |3.433     |Small     |Mid    |
# |43008|0     |7.869     |Small     |High   |
# |43010|0     |3.775     |Small     |Mid    |
# |43011|0     |7.185     |Small     |High   |
# +-----+------+----------+----------+-------+
# only showing top 10 rows
# Figure 2-22 Output of newly created DataFrame with custom columns

# Borrado y renombrando Columnas
# Tú puedes borrar siempre cualquier columna o columnas usando la función drop

# En el ejemplo se declara una lista 'columns_to_drop' de las columnas del DF que se quieren eliminar
columns_to_drop: list = ['budget_cat']
# El cambio se guardara en el DF 'df_with_newcols'
df_with_newcols : pyspark.sql.dataframe.DataFrame = df_with_newcols.drop(*columns_to_drop)

# Observamos que ya no aparece mas la columna 'budget_cat'
# print(df_with_newcols.columns)
# --> ['id', 'budget', 'popularity', 'ratings']

# Para renombrar alguna columna usamos la función withColumnRenamed

df_with_newcols = df_with_newcols.withColumnRenamed('id', 'film_id').withColumnRenamed('ratings', 'film_ratings')
# --> print(df_with_newcols.columns)
# --> ['film_id', 'budget', 'popularity', 'film_ratings']

# Si la intención es cambiar multiples nombres a las columnas intenta el siguiente comando

new_names = [('budget', 'film_budget'), ('popularity', 'film_popularity')]

# Aplicando la funcion alias
df_with_newcols_renamed = df_with_newcols.select(list(map(lambda old,new: col(old).alias(new),*zip(*new_names))))

# Ambos métodos tienen el mismo plan de ejecución, podemos verificar estos cambios
# usando la funcion printSchema o usando .show()

# Terminar la sesión de Spark
spark.stop()

