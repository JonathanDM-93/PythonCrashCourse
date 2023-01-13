# CREAMOS UN DICCIONARIO Y PRACTIQUEMOS CON ALGUNAS MODIFICACIONES
# Los nombres de los tanques fueron obtenidos del juego World Of Tanks Blitz
# El objetivo de este programa es:
# 1.- El usuario ingresa el nivel de tanques que quiere acceder.
# 2.- Creamos un diccionario que almacene una lista de tanques por nivel
# 3. Con un for recorremos todas las llaves y en el if si esta llave coincide con la que el usuario
# ingreso se imprime un mensaje y despues entra en otro for para recorrer los valores dentro de la lista.
# NOTA: Es importante destacar que en el segundo for se declara el iterador (tanque) sobre el diccionario,
# el cual toma la llave correspondiente a la que el usuario ingreso gracias al if e imprime posteriormente los
# valores dentro de la lista correspondiente a esa llave.

searchTank: str = input('¿Que nivel de tanques estas buscando? ')

mi_diccionario: dict = {
    'VII': ['T-34', 'Tiger', 'T-43', 'SU-152', 'Ju-To', 'AMX M4 45'],
    'IX': ['E-75', 'Emil', 'Conqueror', 'Tortoise'],
    'X': ['E-100', 'IS-4', 'FV215b', 'Maus', 'Leopard 1']
}

for llave in mi_diccionario.keys():
    if searchTank == llave:
        print('El nivel es: ' + searchTank)
        for tanque in mi_diccionario[llave]:  # Accede a los valores de la llave que hizo match de la entrada del usuario
            print(tanque)



