# Devuleve todos los objetos/archivos que estan dentro de un bucket especifico
# en este caso estoy llamando a el bucket con el 'nombre sismos-ssn'
import boto3
s3 = boto3.resource('s3')
bucket = s3.Bucket('sismos-ssn')

for obj in bucket.objects.all():
    print(obj.key)

# >>
# SSNMX_catalogo.csv


print('++++++++++++++++')
# S3 list all keys with the prefix 'test-1/'
s3 = boto3.resource('s3')
bucket = s3.Bucket('bucketdevvirginia')
for bucket in s3.buckets.all():
    for obj in bucket.objects.filter(Prefix='01_Contacts.csv'):
        print('{0} : {1}'.format(bucket.name, obj.key))
