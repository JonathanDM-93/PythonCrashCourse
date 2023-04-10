# Librerias
import boto3
from datetime import datetime, timedelta

#-------------------------------------------------#
client = boto3.client('s3')
#-------------------------------------------------#

# Crear nombre de la carpeta del día anterior
date = (datetime.today() - timedelta(days=1)).strftime("%Y/%m/%d")
# print(date) # --> 2023/03/15

newdate = date.replace('/', '')
# print(newdate) # --> 20230315

# Llamar servicio de AWS
s3 = boto3.resource('s3')
bucket = s3.Bucket('sismos-ssn') # Eligió el bucket que se está usando para tener las keys de los archivos


# Crear un folder
carpeta = str(newdate)

# Crea la carpeta de día vencido
carpetaDate = s3.Bucket('sismos-ssn').put_object(Key = carpeta + '/')
# carpetaDate = s3.Bucket('sismos-ssn').put_object(Key = carpeta + '/'+ '01_Contacts.csv') # Toma archivo y guarda en carpeta creada

# print(type(carpetaDate)) --> <class 'boto3.resources.factory.s3.Object'>

#--------------------------------------#
# 1.- Dentro de un mismo bucket
# 2.- Tomar un archivo de esa carpeta
# 3.- Guardarlo en una nueva carpeta


# Tomar el archivo depositado y guardarlo como tomar el archivo y guardarlo


