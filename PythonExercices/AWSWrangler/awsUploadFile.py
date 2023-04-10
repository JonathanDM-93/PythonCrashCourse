# Carga un archivo a un Bucket seleccionado

import boto3

s3 = boto3.resource('s3')

# Upload a new file
# Carga un archivo de mi equipo local a un Bucket en S3
data = open('C:/Users/joni_/Downloads/peliculas.csv', 'rb')
s3.Bucket('sismos-ssn').put_object(Key='peliculas.cvs', Body=data)

