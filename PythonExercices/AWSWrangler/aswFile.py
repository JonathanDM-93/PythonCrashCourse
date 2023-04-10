# Crear una carpeta dentro de un bucket
import boto3

from PythonExercices.AWSWrangler.awsBucket import bucket


def create_folder(cubeta,name_directorio):
    try:
        s3 = boto3.client('s3') # Objeto tipo cliente
        key = name_directorio + '/'  # Definir una ruta
        s3.put_object(Bucket=bucket, Key=key)
        return key

    except Exception as err:
        print(err)

if __name__ == "__main__":

    # Ingresar el nombre del folder donde queremos que se guarde la carpeta
    # sismos-ssn
    callFunc = create_folder('sismos-ssn', Example.title)