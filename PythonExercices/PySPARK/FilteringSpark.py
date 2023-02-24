# Cargar librera
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
# Definamos una lista de las columnas que deseamos imprimir
select_columnas: list = ["id", "budget", "popularity", "release_date", "revenue", "title"]
# Subconjunto que requieren columnas del DATAFRAME
ReadDF = ReadDF.select(*select_columnas)
# ---> ReadDF.show()
# -----------------------------------------------------------------------------------------------#


"""Filtros/Filtrando"""
# Spark ofrece varias formas de filtrar los datos. Anteriormente, utilizamos la
# función filter(). Esto demuestra que tan importante es esta función a menudo
# en operaciones básicas.
# Tú también puedes encontrar la función where() para filtrar. Ambas funciones funcionan
# de la misma manera. Sin embargo, la función filter() es el estandar en Scala para esta función.
# .where() = .filter()

# El siguiente ejemplo se aplica la función.filter para filtrar los títulos que comiencen
# con las letras "Meet"

FilterTitles = ReadDF.filter(ReadDF['title'].like('Meet%'))
# --> FilterTitles.show(10,False)
# Se observa que ahora solo devuelve los libros que inician con la palabra clave "Meet"
# +------+--------+----------+------------+-----------+--------------------------------+
# |id    |budget  |popularity|release_date|revenue    |title                           |
# +------+--------+----------+------------+-----------+--------------------------------+
# |43957 |500000.0|3.004     |2005-06-28  |1000000.0  |Meet The Browns - The Play      |
# |355515|0.0     |0.6       |1953-01-01  |0.0        |Meet Me at the Fair             |
# |279542|0.0     |0.764     |1978-07-01  |0.0        |Meeting in July                 |
# |39997 |0.0     |3.805     |1989-11-15  |0.0        |Meet the Hollowheads            |
# |131504|0.0     |1.259     |1956-03-09  |0.0        |Meet Me in Las Vegas            |
# |386882|0.0     |2.373     |1996-02-09  |0.0        |Meet Me in the Dream: Wonderland|
# |16710 |0.0     |8.892     |2008-03-21  |4.1939392E7|Meet the Browns                 |
# |20430 |0.0     |3.507     |2004-01-29  |0.0        |Meet Market                     |
# |271048|0.0     |0.624     |1937-06-04  |0.0        |Meet the Missus                 |
# |117825|0.0     |2.744     |1991-11-17  |0.0        |Meeting Venus                   |
# +------+--------+----------+------------+-----------+--------------------------------+
# only showing top 10 rows
# Fig 2-17 Filtering matches using "like" expression

# Ahora encontremos que títulos no terminan con "s"
FilterTitles_withoutS = ReadDF.filter(~ReadDF['title'].like('%s'))
# --> FilterTitles_withoutS.show(10,False)
# +-----+------+----------+------------+-------+---------------------------------------+
# |id   |budget|popularity|release_date|revenue|title                                  |
# +-----+------+----------+------------+-------+---------------------------------------+
# |43000|0     |3.892     |1962-05-23  |0      |The Elusive Corporal                   |
# |43001|0     |5.482     |1962-11-12  |0      |Sundays and Cybele                     |
# |43002|0     |8.262     |1962-05-24  |0      |Lonely Are the Brave                   |
# |43003|0     |7.83      |1975-03-12  |0      |F for Fake                             |
# |43004|500000|5.694     |1962-10-09  |0      |Long Day's Journey Into Night          |
# |43006|0     |2.873     |1962-03-09  |0      |My Geisha                              |
# |43007|0     |3.433     |1962-10-31  |0      |Period of Adjustment                   |
# |43008|0     |7.869     |1959-03-13  |0      |The Hanging Tree                       |
# |43010|0     |3.775     |1962-01-01  |0      |Sherlock Holmes and the Deadly Necklace|
# |43011|0     |7.185     |1962-01-01  |0      |Sodom and Gomorrah                     |
# +-----+------+----------+------------+-------+---------------------------------------+
# only showing top 10 rows
# Figure 2-18 Filtering non-matches using "like" expression

# Ahora si nosotros queremos encontrar cualquier título que contenga las letras "ove"
# nosotros deberíamos usar la función rlike() como una función regular

FilterTitles_with_ove = ReadDF.filter(ReadDF['title'].rlike('\w*ove'))
# --> FilterTitles_with_ove.show(10,False)

# +-----+--------+------------------+------------+---------+------------------------+
# |id   |budget  |popularity        |release_date|revenue  |title                   |
# +-----+--------+------------------+------------+---------+------------------------+
# |43086|0       |2.5700000000000003|2002-01-01  |0        |Dead Above Ground       |
# |43100|0       |6.939             |1959-10-07  |0        |General Della Rovere    |
# |43152|0       |5.513             |2001-06-21  |0        |Love on a Diet          |
# |43191|0       |5.813             |1952-08-29  |0        |Beware, My Lovely       |
# |43281|0       |2.186             |1989-11-22  |0        |Love Without Pity       |
# |43343|0       |2.683             |1953-11-26  |0        |Easy to Love            |
# |43347|30000000|25.27             |2010-11-22  |102820008|Love & Other Drugs      |
# |43362|0       |2.006             |1952-02-23  |0        |Love Is Better Than Ever|
# |43363|0       |1.6840000000000002|1952-05-29  |0        |Lovely to Look At       |
# |43395|0       |2.43              |1950-11-10  |0        |Two Weeks with Love     |
# +-----+--------+------------------+------------+---------+------------------------+
# only showing top 10 rows
# Figure 2-19. Filtering matches using regular expression

# Otra forma también de reescribir la expresión anterior es:
# Carga el DF aplica la función filter -- del DF toma el campo title y si contiene 'ove'
# los toma y filtra el resto.
FilterTitles_with_ove_2dot0 = ReadDF.filter(ReadDF.title.contains('ove'))
# --> FilterTitles_with_ove_2dot0.show(10,False)
# +-----+--------+------------------+------------+---------+------------------------+
# |id   |budget  |popularity        |release_date|revenue  |title                   |
# +-----+--------+------------------+------------+---------+------------------------+
# |43086|0       |2.5700000000000003|2002-01-01  |0        |Dead Above Ground       |
# |43100|0       |6.939             |1959-10-07  |0        |General Della Rovere    |
# |43152|0       |5.513             |2001-06-21  |0        |Love on a Diet          |
# |43191|0       |5.813             |1952-08-29  |0        |Beware, My Lovely       |
# |43281|0       |2.186             |1989-11-22  |0        |Love Without Pity       |
# |43343|0       |2.683             |1953-11-26  |0        |Easy to Love            |
# |43347|30000000|25.27             |2010-11-22  |102820008|Love & Other Drugs      |
# |43362|0       |2.006             |1952-02-23  |0        |Love Is Better Than Ever|
# |43363|0       |1.6840000000000002|1952-05-29  |0        |Lovely to Look At       |
# |43395|0       |2.43              |1950-11-10  |0        |Two Weeks with Love     |
# +-----+--------+------------------+------------+---------+------------------------+
# only showing top 10 rows
# Vemos que tenemos el mismo resultado

# Hay ciertas situaciones en las que tenemos cientos de columnas y solo queremos
# identificar un subgrupo de columnas a traves de un prefijo o sufijo.
# Podemos conseguirlo usando la función colRegex identificar campos que inicien
# con las letras 're'

RegexFuncion_re = ReadDF.select(ReadDF.colRegex("`re\w*`"))
# --> RegexFuncion_re.printSchema()
# root
#  |-- release_date: string (nullable = true)
#  |-- revenue: string (nullable = true)
# Figure 2-20 Filtering columns by prefix using regular expressions


# Ahora queremos buscar ciertos campos que terminen con la letra 'e'
RegexFuncion_e = ReadDF.select(ReadDF.colRegex("`\w*e`"))
# --> RegexFuncion_e.printSchema()
# root
#  |-- release_date: string (nullable = true)
#  |-- revenue: string (nullable = true)
#  |-- title: string (nullable = true)
# Figure 2-21 Filtering columns by suffix using regular expressions

"""
Regex can be confusing, so let’s have a brief refresher on the topic. In general, 
we can identify all the characters and numerics by metacharacters. Regex uses these 
metacharacters to match any literal or alphanumeric expression. Here is a short list of 
the most-used metacharacters:
Single characters:
• \d – Identifies numbers between 0 and 9
• \w – Identifies all upper- and lowercase alphabets and numbers from 
0 to 9 [A–Z a–z 0–9]
• \s – Whitespace
• . – Any character
We also have a set of quantifiers that guide how many characters to search, as 
follows:
Quantifiers:
• * – 0 or more characters
• + – 1 or more characters
• ? – 0 or 1 characters
• {min,max} – specify the range, any characters between the range 
including min, max
• {n} – Exactly n characters
If you look back at both the earlier expressions, you will see that we have made use 
of \w, indicating we want to match all alphanumeric characters, ignoring the case. In the 
expression where we wanted to identify variables with the “re” prefix, \w was followed by 
the quantifier * to indicate we wanted to include all characters after “re.”
"""
# Terminar la sesión de Spark
spark.stop()