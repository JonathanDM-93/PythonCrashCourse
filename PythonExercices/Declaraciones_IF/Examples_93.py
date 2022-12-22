# Ejemplos del TRY IT YOURSELF PÁGINA 93

# Vamos a reforzar lo anterior creando algunos ejercicios.
# Creamos una lista con algunos nombres de usuarios

UsersList: list = ['Jonathan', 'Francisco', 'Peter', 'Olab', 'Karla']

# En este caso Peter es el administrador y queremos que cuando el loop se encuentre con
# el administrador devuelva un mensaje. Para los demás dara otro mensaje.


for item in UsersList:
    if item == 'Peter':
        print('** Hola peter, ¿Deseas ver tus pendientes de hoy? **')
    else:
        print('Gracias por ingresar: ' + item)

print('\n[*]\n')

# En el siguiente ejemplo crearemos dos listas que contengan nombres de usuarios registrados
# y otra lista de seran nombres de usuarios nuevos compararemos una con otra y mandaremos un
# MENSAJE para comentar si el nombre ya se encuentra registrado


UserRegi: list = ['Jonathan', 'Peter', 'Maria', 'Karen', 'Nadia']
NewUser: list = ['Maria', 'Nadia', 'Kevin']

for item in NewUser:
    if item in UserRegi:
        print('Elige un nuevo nombre')
    else:
        print('El nombre que elegiste no se repite')

# Lo que se quiere dar a entender en el ejemplo es que se puede comparar dos listas y si dentro
# de ellas se encuentra un elemento idéntico
# en este caso lo que se imprime es:

# Elige un nuevo nombre
# Elige un nuevo nombre
# El nombre que elegiste no se repite

# Porque dos de los nombres se repiten y el último no.

print('\n[*]\n')

# En el último ejemplo crearemos una lista con los numeros ordinales y crearemos una cadena
# if-elif-else para que dependiendo del número que ingrese el usuario devuelva su posición
# 1st, 2nd, 3rd, 4th etc.

IngresaNum: str = input('Ingresa un número: ')
if IngresaNum == str(0):
    print('Cero es invalido')
elif IngresaNum < str(2):
    print(IngresaNum + 'st')
elif IngresaNum < str(3):
    print(IngresaNum + 'nd')
elif IngresaNum < str(4):
    print(IngresaNum + 'er')
else:
    print(IngresaNum + 'th')

# Observamos que después del 3 todos los demás numeros terminan con th


print('\n[*]\n')

# En este ejemplo tenemos una lista de y queremos utilizar la cadena if-elif-else para poder imprimir
# correctamente los números con su correspondiente posición 1st, 2nd, 3er etc.

Nums: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for item in Nums:
    if item == 1:
        print(str(item) + 'st')
    elif item == 2:
        print(str(item) + 'nd')
    elif item == 3:
        print(str(item) + 'er')
    else:
        print(str(item) + 'th')

