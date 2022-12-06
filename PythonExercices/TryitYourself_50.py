# TRY IT YOURSELF pag 50
# En ocasiones es necesario organizar tus listas, para esto veremos los siguientes métodos.
# Crearemos una lista  de autos de la marca Toyota:

ToyotaList: list = ['Yaris', 'Corolla', 'Camry', 'Tundra', 'Avanza']
# Utlizaremos el método .sort() para organizar la lista alfabéticamente

ToyotaList.sort()
print(ToyotaList)
# 'Avanza', 'Camry', 'Corolla', 'Tundra', 'Yaris']
# Observamos que la lista ahora esta organizada de forma alfabético y de forma permanente
# Para indicar si queremos que se ordene de forma ascendente o descentente pasamor el argumento reverse = True or False

ToyotaList.sort(reverse=True)
print(ToyotaList)
# ['Yaris', 'Tundra', 'Corolla', 'Camry', 'Avanza']

ToyotaList.sort(reverse=False)
print(ToyotaList)
# ['Avanza', 'Camry', 'Corolla', 'Tundra', 'Yaris']

print('\n[*]\n')

# Ahora si queremos que solo de forma temporal se organice una lista usamos la función sorted()
# Creamos una lista nueva con las letras del alfabeto desordenada.

newList: list = ['W', 'N', 'P', 'Z', 'A']
# Aplicamos la función sorted()
print('Es la lista ordenada: ' + str(sorted(newList)))
# Es la lista ordenada: ['A', 'N', 'P', 'W', 'Z']

print('Es la lista original: ' + str(newList))
# Es la lista original: ['W', 'N', 'P', 'Z', 'A']
# Vemos que al usar la función imprime la lista ordenada pero si imprimimos nuevamente la lista la muestra como
# originalmente se encontraba.

print('\n[*]\n')

# A continuación utilizaremos el método reverse() la cual devuelve la lista iniciando la lista a partir del ultimo
# valor que se ingreso en la lista.

enterList: list = ['Enter [0]', 'Enter [1]', 'Enter [2]', 'Enter [3]', 'Enter [4]']
enterList.reverse()
print('REVERSE: ' + str(enterList))
# ['Enter [4]', 'Enter [3]', 'Enter [2]', 'Enter [1]', 'Enter [0]']
# Vemos que incia la lista desde el ultimo elemento que se ingreso para regresar al estado original en este caso
# podemos utilizar nuevamente el método .reverse()

enterList.reverse()
print('ORIGINAL: ' + str(enterList))

print('\n[*]\n')

# Finalmente si queremos saber la longitud de cualquier lista podemos usar la función len()
print(len(enterList))
# 5
# La lista contiene 5 elementos.

