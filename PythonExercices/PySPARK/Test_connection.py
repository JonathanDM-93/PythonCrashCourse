# Crear una conexión a REDSHIFT
from pyspark import SparkContext
from pyspark.sql import SQLContext

spark = SparkContext(master="local", appName="Test_connection")
sqlContext = SQLContext(spark)

# Read data from a table
"""df = sqlContext.read \
    .format("io.github.spark_redshift_community.spark.redshift") \
    .option("url", "jdbc:redshift://mycluster.cfvkjcuj27ud.us-east-1.redshift.amazonaws.com:5439/dev") \
    .option("dbtable", "sales") \
    .option("tempdir", "s3n://jonathancubeta/tickitdb") \
    .option("aws_iam_role", "arn:aws:iam::869215270926:role/Jonathan_Rol") \
    .load()"""

# Read data from a query
"""df = sqlContext.read \
    .option("url", "jdbc:redshift://mycluster.cfvkjcuj27ud.us-east-1.redshift.amazonaws.com:5439/dev") \
    .option("query", "select x, count(*) sales") \
    .option("tempdir", "s3n://jonathancubeta/tickitdb") \
    .option("aws_iam_role", "arn:aws:iam::869215270926:role/Jonathan_Rol") \
    .load()"""

# Read data from a table
df = sqlContext.read\
    .option("url", "jdbc:redshift://mycluster.cfvkjcuj27ud.us-east-1.redshift.amazonaws.com:5439/dev") \
    .option("dev", "sales") \
    .option("tempdir", "s3://jonathancubeta/tickitdb") \
    .load()

df.show()