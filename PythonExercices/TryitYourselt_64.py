# TRY IT YOURSELF pag 64
# En esta ocasión no crearemos listas con string, ahora almacenaran números
# Para crear una serie de números dentro de una lista podemos auxiliarnos
# de la función range()


for item in range(0, 10):
    print(item)

print('\n[*]\n')

# Pero lo anterior es un codigo muy simple, vamos a guardar esos números en
# una lista

newList: list = []  # Lista vacia
for item in range(0, 11):
    newList.append(item)
print(newList)
# Ahora si la lista esta almacenada en una variable llamada newList

print('\n[*]\n')

# Ahora digamos que queremos una lista que comience en 0 y termine en 100, pero
# que de saltos de 10 en 10

jumpList: list = []
for item in range(0, 110, 10):
    jumpList.append(item)
print(jumpList)
# Observamos que en la linea 23 dentro de los parentesis del for
# el 0 indica el inicio de la lista, el 110 el limite de la lista
# y el 10 es el salto que dara.

print('\n[*]\n')

# Ahora por ejemplo queremos que a cada elemento dentro de una lista se
# eleve al cuadrado.

sqrt: list = []
for item in range(0, 110, 10):
    square: int = item ** 2
    sqrt.append(square)
print(sqrt)
# En el ejemplo anterior observamos que la multiplicación de cada elemento de la lista
# se guarda en una variable llamada square y este nuevo valor en la variable se
# almacena en la lista sqrt.

print('\n[*]\n')

# Existen funciones que nos permiten obtener algunas parametros como el minimo
# maximo o la suma de los elementos de nuestra lista
# Estas funciones son:
suma: int = sum(sqrt)
print('Suma de los elementos: ' + str(suma))
minimo: int = min(sqrt)
print('Minimo de los elementos: ' + str(minimo))
maximo: int = max(sqrt)
print('Máximo de los elementos: ' + str(maximo))

# NOTA: tomamos la lista del anterior ejercicio

print('\n[*]\n')

# Existe una sintaxis diferente para escribir los loops

example: list = [valorexp**2 for valorexp in range(1, 11)]
print(example)
# Dentro de los corchetes primero se indica la el indicador que apunta a cada
# elemento dentro de la lista, despues se ejecuta el for para cada elemento dentro
# de la lista.
