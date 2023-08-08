# Librerias
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.sql import SparkSession
import boto3


                                    # ----------------- SEPARADOR -----------------#

# Crear sesión
# spark = SparkSession.builder.appName("Data").getOrCreate()

sc = SparkContext("local", "SomeName")
sql_context = SQLContext(sc)


secretsmanager_client = boto3.client('secretsmanager')
secret_manager_response = secretsmanager_client.get_secret_value(
    SecretId='string',
    VersionId='string',
    VersionStage='string'
)
username = 'jrosam'
password = 'C083pD709lBx'
url = "jdbc:redshift://devcluster.c1spmqqqye1u.us-east-1.redshift.amazonaws.com:5439/devsie?user=" + username + "&password=" + password

# Conexión al Cluster
# jdbc:redshift://devcluster.c1spmqqqye1u.us-east-1.redshift.amazonaws.com:5439/devsie


# Read data from a table
df = sql_context.read \
    .format("io.github.spark_redshift_community.spark.redshift") \
    .option("url", url) \
    .option("dbtable", "ratv.hr_tp_kan_channels") \
    .option("tempdir", "s3://path/for/temp/data") \
    .load()