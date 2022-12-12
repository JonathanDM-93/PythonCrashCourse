# TRY IT YOURSELF pág. 64
# En esta séccion aprenderemos como trabajar a traves de todos los elementos de una lista.
# Podemos trabajar con un grupo especifico de elementos en una lista a esto se le llama slice.

# Recordando la clase anterior ¿Cómo creamos una lista númerica?
makeList: list = []
for item in range(0, 11, 1):
    makeList.append(item)
print(makeList)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('\n[*]\n')

# Querer insertar un elemento un un sitio predefinido
makeList[3] = 100
print(makeList)
# [0, 1, 2, 100, 4, 5, 6, 7, 8, 9, 10]

print('\n[*]\n')

makeList.insert(2, 3)  # Esto indica en el lugar [2] agrega el 3
print(makeList)
# [0, 1, 3, 2, 100, 4, 5, 6, 7, 8, 9, 10]

print('\n[*]\n')

# Ahora bien para continuar con el topico de manejar una fracción de los elementos de una lista
# Crearemos una lista con algunos módelos de celulares.

celphoneList: list = ['Iphone', 'Motorola', 'Samsumg', 'Nokia', 'Oppo']
selectItem: list = celphoneList[2:]
print(selectItem)
# ['Samsumg', 'Nokia', 'Oppo']
# En este ejemplo cree una nueva variable para almacenar los elementos que estuvieran en los lugares 2 en adelante.

print('\n[*]\n')

# Tambien podemos llamar a los elementos a traves de indices negativos
print(celphoneList[-3:])
# ['Samsumg', 'Nokia', 'Oppo']

print('\n[*]\n')

# Si quisieramos traer algunos elementos de la lista celphoneList en un loop hacemos lo siguiente:
for item in celphoneList[:3]:
    print('El teléfono es: ' + item)
# Como observamos ahora solo traemos ciertos elementos dentro de la lista celphoneList.

print('\n[*]\n')

# Sigamos con los ejemplos, esta vez veremos como generar una copia de una lista [:] indicando con corchetes y en el
# interior dos puntos.

foodList: list = ['Pizza', 'Hamburguesa', 'Alitas', 'Tacos']
copyList: list = foodList[:]  # Estamos indicando que queremos una copia de foodList
print(foodList, '<-MISMA LISTA->', copyList)
# ['Pizza', 'Hamburguesa', 'Alitas', 'Tacos'] <-MISMA LISTA-> ['Pizza', 'Hamburguesa', 'Alitas', 'Tacos']

print('\n[*]\n')



