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

