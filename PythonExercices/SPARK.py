# ---------------------------------------------------------#
# Mecanismos para interactuar con SPARK

# Libreria para la session de Spark permite tener mejores formas de configuración
from pyspark.sql import SparkSession

# La libreria para el SparkContext
#from pyspark import SparkContext

# ------------------------------------------------------- #
# Librerias para crear la estructura de los DATAFRAME
#from pyspark.sql.types import StructType, StructField
#from pyspark.sql.types import IntegerType, StringType
#from pyspark.sql.types import Row

# ------------------------------------------------------- #

# Crear la sesión de Spark
spark = SparkSession \
    .builder \
    .appName("SPARK") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# Crear el contexto de Spark/punto de conexión para todo spark


# cargar el archivo .csv
df = spark.read.load("C:/Users/joni_/Downloads/juegos.csv", format="csv", sep=",", inferSchema="true", header="true")

df.show()



# Terminar la sesión de Spark
spark.stop()
