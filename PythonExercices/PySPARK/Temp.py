from pyspark.sql import SQLContext
from pyspark import SparkContext, SparkConf
import boto3

spark = SparkContext(master="local", appName="Temp").getOrCreate()
sqlContext = SQLContext(spark)

conf = SparkConf().setAppName("test").setMaster("local")
sc = SparkContext(conf=conf)

secretsmanager_client = boto3.client('secretsmanager')
secret_manager_response = secretsmanager_client.get_secret_value(
    SecretId='string',
    VersionId='string',
    VersionStage='string'
)
username = "mycluster"
password = "Zamusmetroid10#"
url = "jdbc:redshift://redshifthost:5439/database?user=" + str(username) + "&password=" + str(password)

# Read data from a table
df = sqlContext.read \
    .format("io.github.spark_redshift_community.spark.redshift") \
    .option("url", "jdbc:redshift://mycluster.cfvkjcuj27ud.us-east-1.redshift.amazonaws.com:5439/dev") \
    .option("dbtable", "dev.sales") \
    .option("tempdir", "s3://jonathancubeta/tickitdb") \
    .load()

df.show()