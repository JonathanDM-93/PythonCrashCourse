# Un tema interesante en lo que se llama compresión de diccionarios o Dictionary Comprehension
# Veamos un ejemplo de como podemos agregar valores a un diccionario a traves de un for
# EJEMPLO 1

classicDictionary: dict = {}
for item in range(1, 5):
    classicDictionary[item] = item * 2
# print(classicDictionary)
# >> {1: 2, 2: 4, 3: 6, 4: 8}

# Una segunda forma seria:
updateDictionary: dict = {item: item * 2 for item in range(1, 5)}
# print(updateDictionary)
# >> {1: 2, 2: 4, 3: 6, 4: 8}
# Observamos que las dos formas hacen exactamente lo mismo pero en la 2da forma
# utilizamos menos líneas de código.

# EJEMPLO 2
# Recorremos una lista de paises la cual sirve para asignarle a la CLAVE del
# Diccionario un valor de población usando la libreria random

import random

paises: list = ['México', 'Holanda', 'Perú', 'Alemania']
poblacion: dict = {}

for pais in paises:
    poblacion[pais] = random.randint(1, 10000)
# print(poblacion)

# Ahora haciendo lo mismo que arriba pero con comprensión de diccionarios

updatePoblacion: dict = {pais: random.randint(1,10000) for pais in paises}
# print(updatePoblacion)
# {'México': 2488, 'Holanda': 9999, 'Perú': 9606, 'Alemania': 8393}

# EJEMPLO 3
# Generar un diccionario a partir de dos listas
# Primero hagamos dos listas
# 1.- Lista con modelos de carros de la marca Toyota
ToyotaList: list = ['Yaris', 'Corolla', 'Camry', 'Tundra', 'Avanza']

# 2.- Lista con los precios de los modelos de los carros
PriceList: list = [100000, 250000, 528000, 631000, 410000]

# 3.- Unir las dos listas
MergeList: list = list(zip(ToyotaList, PriceList))

# 4.- Crear el diccionario
# Agreagr un LLAVE-VALOR al diccionario 
CompleteList: dict = {modelo: precio for (modelo, precio) in MergeList}
# print(CompleteList)
# >>
# {'Yaris': 100000,
# 'Corolla': 250000,
# 'Camry': 528000,
# 'Tundra': 631000,
# 'Avanza': 410000}

