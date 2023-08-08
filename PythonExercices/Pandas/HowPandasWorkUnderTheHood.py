# Como funciona PANDAS por debajo
# Es importante en cualquier lenguaje de programación entender que es lo que sucede por debajo
# esto ayuda a escribir codigo de forma explícita, simple, eficaz y correcta.

# Es importante entender las estructuras de datos para usar las optimizaciones
# disponibles.
# Empecemos con los sets los cuales son iterables, pero inmutables
# Este tipo de estructura de datos es buena para almacenar infomacion estatica
# como metadata.

lista: list = [0,1,2,20]
lista[3] = 3
print(lista)

arreglo : set = {8, 25, 0.998}

for i in arreglo:
    print(i + 1)

tuplas : tuple = ( 1, 2, "Hola")
print(tuplas[0])

# Eligiendo el tipo correcto de DF
# ¿Qué tipo de procesamiento de datos se realizara con los datos?
# ¿Necesitarás ejecutar calculos de agregación sobre la data o agruparla?

import pandas as pd

restaurante_inspeccion = pd.DataFrame ({
    "restaurante" : ["Dinner", "Dinner","Pandas","Pandas"],
    "localidad" : [(4,2),(4,2),(5,4),(5,4)],
    "fecha" : ["02/18", "05/18", "02/18", "05/18"],
    "puntaje" : [90, 100, 55, 60],
})

print(restaurante_inspeccion)

print('\n*****')
# Se seleccionan dos campos del DF y se agrupan
total_inspectiones = restaurante_inspeccion.groupby(
    ["restaurante", "localidad"], as_index=False,)["puntaje"].count()

print(total_inspectiones)

print('\n*****')

# Cambio de nombre de los campos del DF
total_inspectiones.rename(columns={"puntaje":"total"}, inplace=True)
print(total_inspectiones)

print('\n*****')
restaurante_inspeccion = pd.merge(
    restaurante_inspeccion,
    total_inspectiones,
    how="outer",
)

print(restaurante_inspeccion)

print('\n*****')
#Guardando la data en un Multi-index
restaurante = pd.MultiIndex.from_tuples(
    (
    ("Diner", (4,2)),
    ("Diner", (4,2)),
    ("Pandas", (4,2)),
    ("Pandas", (4,2)),
),
    names=["restaurante", "location"],
)

print(restaurante)


