# Iniciando un nuevo cápitulo, abordaremos la declaración if
# Cuando programamos a menudo queremos agregar condiciones y decidir cuál acción
# se debe tomar con base a alguna condición.

# Imaginemos que tenemos una llantera y tenemos en existencia los siguientes modelos:
ListWheels: list = ['Bridgestone', 'Continental', 'Firestone', 'Michelin', 'Goodyear']


# Buscaremos dentro de nuestra lista el modelo que pidio el cliente
for item in ListWheels:
    if item == 'Michelin':
        print(item.upper())
    else:
        print(item.lower())

# bridgestone
# continental
# firestone
# MICHELIN
# goodyear

# Vemos que imprime los elementos de la lista y cuando la condición es verdadera imprime el elemento en mayúsculas
# y cuando es falso imprime el resto de los demás elementos en minuscula.

print('\n[*]\n')

# En el ejercicio anterior observamos que el condicional busca una iguldad y si esto
# resulta verdadero se imprime un mensaje
# En esta ocasión veremos las desigualdades !=

Nombre: str = input('Ingresa un nombre: ')
if Nombre != 'Zaz':
    print(Nombre + 'Es un nombre diferente a Zac')

print('\n[*]\n')

# Si ingresamos un nombre pj. Ana al entrar en la condición vemos que efectivamente
# el nombre es diferente a Zac y la condición es True y se ejecuta la acción del
# print()

# También podemos hacer comparaciones con números
EnterNumero: str = input('Ingresa un número: ')
if EnterNumero != str(100):
    print('Este no es el número correcto.')
else:
    print('Es el numero correcto!')
# Vemos que si el número es diferente de 100 se imprime el primer mensaje
# Si el número es idéntico al que está almacenado se imprime el segundo mensaje

print('\n[*]\n')

# Ahora bien, en ocasiones es importante de antemano conocer si algún elemento
# se encuentra dentro de una lista antes de ejecutar alguna acción.
Buscar: str = input('Que elemento buscas: ')
elementoQuimico: list = ['Oro', 'Plata', 'Titanio']
for item in elementoQuimico:
    if item == Buscar:
        print('True')
    else:
        print('False')

print('\n[*]\n')

# Esta es una manera de verificar si un elemento que busca un usuario se
# encuentra en una lista o no
# A continuación presentaremos otra forma usando otra lista.
AutosBusqueda: str = input('¿Qué auto buscas?: ')
ToyotaList: list = ['Yaris', 'Corolla', 'Camry', 'Tundra', 'Avanza']
if AutosBusqueda not in ToyotaList:
    print('El valor no se encuentra en la lista y la condición es verdadera y \n'
          'se imprime este mensaje')
else:
    print('Si se encuentra el auto por lo que la condición es falsa.')

# Vemos que se usa el prefijo NOT


