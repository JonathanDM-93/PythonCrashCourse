# Listar todos los buckets en S3

import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

# >>
# bucketdevvirginia
# bucketorigenes
# cubetadestino
# cubetaincial
# hrrawextendido
# jonathancubeta
# sismos-ssn

client = boto3.client('s3')
response = client.get_object(
    Bucket='sismos-ssn',
    Key='01_Contacts.csv',
    Range='bytes=0-9',
)

print(response)
