# Copia los archivos de un bucket a otro en sus respectivas carpetas
# https://aws-sdk-pandas.readthedocs.io/en/stable/stubs/awswrangler.s3.copy_objects.html#awswrangler.s3.copy_objects
import awswrangler as wr
wr.s3.copy_objects(
    paths=["s3://numerone/dir0/jc-listings.csv", "s3://numerone/dir0/ny-listings.csv"], # Agregar los elementos que se desean copiar
    source_path="s3://numerone/dir0/", # Ruta fuente
    target_path="s3://numerodos/dir1/" # Ruta destino
)

# Lista todos los objetos dentro de un Bucket
listObj = wr.s3.list_objects('s3://numerone/')
print(listObj)

# Ahora vamos a borrarlos
wr.s3.delete_objects(['s3://numerodos/dir1/jc-listings.csv', 's3://numerodos/dir1/ny-listings.csv'])  # Delete both objects
