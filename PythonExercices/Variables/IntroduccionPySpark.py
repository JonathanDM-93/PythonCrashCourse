# Crear Sesion de spark
from pyspark.sql import SparkSession
spark =SparkSession.builder.appName('IntroduccionPySpark').getOrCreate()

# Se necesita el SQLContext para programar DATAFRAMES
# from pyspark.sql import SQLContext
# Cree un SQLContext a pasando como arguemnto a la sessión
# sql_context = SQLContext(spark)


# cargar el archivo .csv el cual ya es un DF
df = spark.read.load("C:/Users/joni_/Downloads/peliculas.csv",
                     format="csv", sep=",",
                     inferSchema="true",
                     header="true")

# Crear un esquema en Python






df.show()

# print(type(df))
# <class 'pyspark.sql.dataframe.DataFrame'>




