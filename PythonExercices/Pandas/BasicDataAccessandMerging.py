# BASIC DATA ACCESS AND MERGGING
# Hay varias formas de accesar y unir DF con PANDAS
# En este capítulo se cubrirá los metodos basicos pata obtener la data fuera
# de un DF, crear un SUB-DF y unir entre si DF.
import pandas

# La creación de un DF es similar a un diccionario
# Bueno solo puse un pequeño ejemplo de la estructura de un diccionario
# y como se acceden a sus elementos.

myDict : dict = {
    "vehiculos" : ["vento","polo","versa"],
    "celulares" : ["iphone","samsumg"],
}

# Imprimir las llaves
"""for keys in myDict.keys():
    print(keys)"""

# Imprimir las items
"""for items in myDict.items():
    print(items)"""


# LISTING 2-1. Ejemplo de la sintaxis de diccionario

import pandas as pd

account_info = pd.DataFrame({
    "name" : ["Bob", "Mary", "Mita"],
    "account" : [123846, 123972, 347209],
    "balance" : [123, 3972, 7209],
})

"""print(account_info["name"])"""
# 0     Bob
# 1    Mary
# 2    Mita
# Name: name, dtype: object

# ---- SEPARATOR ---- #

account_info["name"] = ["Smith", "Jane" ,"Patel"]

"""print(account_info)"""
# name  account  balance
# 0  Smith   123846      123
# 1   Jane   123972     3972
# 2  Patel   347209     7209

# ---- SEPARATOR ---- #

# LISTING 2-2. Ejemplo de crear un sub-DataFrame

sub_account_info = account_info[["name", "balance"]]
"""print(sub_account_info)"""
# name  balance
# 0  Smith      123
# 1   Jane     3972
# 2  Patel     7209

# Método iloc
# Se pueden acceder a los renglones del DF a través del método iloc el cual usa
# una sintaxis de lista

# LISTING 2-3. Ejemplo para acceder a los renglones en un DF

# Usaremos el DF account_info y declarado anteriormente

# account_info = pd.DataFrame({
#     "name" : ["Smith", "Jane", "Patel"],
#     "account" : [123846, 123972, 347209],
#     "balance" : [123, 3972, 7209],
# })

"""print (account_info.iloc[1])"""
# name         Jane
# account    123972
# balance      3972
# Name: 1, dtype: object

"""print(account_info.iloc[0:2])"""
#     name  account  balance
# 0  Smith   123846      123
# 1   Jane   123972     3972

# El método iloc es usado para acceder al índice del DF.
# La primera posición en el método iloc específica los índices de los renglones
# mientras que la segunda posición hace referencia a los índices de la columna.

"""print(account_info.iloc[1,2])"""
# 3972

# Lo que dice lo siguiente es: Devuelve todos los renglones de las columnas 0 y 2
"""print(account_info.iloc[:, [0, 2]])"""
#     name  balance
# 0  Smith      123
# 1   Jane     3972
# 2  Patel     7209

# iloc también acepta arreglos booleanos.
# LISTING 2-5. Ejemplo para accesar a renglones y columnas en un DF usando iloc

