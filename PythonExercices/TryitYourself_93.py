# TRY IT YOURSELF pág. 93
# Usando declaraciones if en listas
# Como ejemplo tendremos una lista de autos y el usuario preguntara
# si está dentro de la lista

QueryUser: str = input('¿Qué auto deseas buscar?: ')
listCar: list = ['Vento', 'Ibiza', 'Jeep']
for item in listCar:
    if item == QueryUser:
        print('El carro que buscas si esta')
    else:
        print('Los autos que estan en la lista son: ' + item)


# Aqui el programa recibe del usuario el modelo del auto que quiere buscar
# Se recorre la lista a traves del for, si el elemento coincide con el modelo que busca el usuario
# la condición es verdadera y se imprime el mensaje 'El carro que buscas si esta'
# si la condición es falsa se imprime el resto de los mensajes.

print('\n[*]\n')

# Como ver si una lista está vacía o no
# Crearemos dos listas una vacía y otra con algunos elementos para entenderlo un poco mejor

empyList: list = []
if empyList:
    print('Lista vaciá.')
else:
    print('** Lista vaciá **')

# '** Lista vaciá **'
# vemos que aqui se imprime el Segundo mensaje lo que significa que la condición es falsa que la lista no tiene nada

print('\n[*]\n')

noEmpty: list = ['item1', 'item2']
if noEmpty:
    print('// Lista no vaciá //')


