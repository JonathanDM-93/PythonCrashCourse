# Crear una conexión a REDSHIFT
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Connector") \
    .enableHiveSupport() \
    .getOrCreate()

# Read data from a table
DF_Sales = (spark.read
                   .format("io.github.spark_redshift_community.spark.redshift")
                   .option("url", "jdbc:redshift://mycluster.cfvkjcuj27ud.us-east-1.redshift.amazonaws.com:5439/dev")
                   .option("dbtable", "dev.sales")
                   .option("tempdir", "s3://jonathancubeta/tickitdb")
                   .load())

DF_Sales.show()