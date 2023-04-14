# El objetivo de este scrip es que si se necesita crear tablas desde cero se tengan
# los fundamentos técnicos y ejemplos para su creación y las librerias necesarias
# el siguiente enlace se usa de referencia: https://spark.apache.org/docs/2.4.0/sql-data-sources-hive-tables.html

# Cargar libreras
from pyspark.sql import SparkSession
from os.path import expanduser, join, abspath
from pyspark.sql import Row
# warehouse_location points to the default location for managed databases and tables
warehouse_location = abspath('spark-warehouse')


spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration example") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

# spark is an existing SparkSession
spark.sql("CREATE TABLE IF NOT EXISTS src (key INT, value STRING) USING hive").show()

# spark.sql("LOAD DATA LOCAL INPATH 'examples/src/main/resources/kv1.txt' INTO TABLE src")
