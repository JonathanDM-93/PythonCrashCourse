# Cargar librera

from pyspark.sql import SparkSession
# Crear sesión
spark = SparkSession.builder.appName("Data_Wrangling").getOrCreate()
# El tipo de archivo PySpark puede leer otros formatos como: json, parquet, orc
# Cargar el archivo

# Define the data
data = [
    ("00000000000028202015", "00736716", 3, 6692666.48574607, ["20929527","C518970"], 49391.79099499288, 38027.91350092004),
    ("00000000000028202015", "B9383757", 2, 3346214.14328481, ["98394762","20929527"], 20072.333273891494, 38027.91350092004),
    ("00000000000028202015", "00021180040654355390", 2, 3407977.98883373, ["10535398","98394762"], 22273.552269713953, 38027.91350092004),
    ("00000000000028202015", "49377183", 2, 2023324.38079835, ["98394762","17329462"], 59998.56143984353, 38027.91350092004),
    ("00000000000028202015", "83727650", 2, 5474762.65764996, ["C4275938","20929527"], 19654.735789944567, 38027.91350092004)
]

# Define the schema
schema = ["graph_relation_transf_cust1_id", "graph_relation_transf_cust_id", "num_nodes", "idf_raw", "nodes", "norm_2_a", "norm_2_b"]

# Create DataFrame
df = spark.createDataFrame(data, schema)

# Show DataFrame
df.show()