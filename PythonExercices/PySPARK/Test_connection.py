# Crear una conexión a REDSHIFT
from pyspark import SparkContext
from pyspark.sql import SQLContext

spark = SparkContext(master="local", appName="Test_connection")
sqlContext = SQLContext(spark)

# Read data from a table
DataFrame_Sales = sqlContext.read \
    .format("io.github.spark_redshift_community.spark.redshift") \
    .option("url", "jdbc:redshift://mycluster.cfvkjcuj27ud.us-east-1.redshift.amazonaws.com:5439/dev") \
    .option("dbtable", "tickitdb.sales") \
    .option("tempdir", "s3://jonathancubeta/tickitdb") \
    .load()

DataFrame_Sales.show()