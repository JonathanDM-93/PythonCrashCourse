# CREAMOS UN DICCIONARIO Y PRACTIQUEMOS CON ALGUNAS MODIFICACIONES
# El objetivo de este programa es:
# 1.- El usuario ingresa el nivel de tanques que quiere acceder.
# 2.- Creamos un diccionario que almacene una lista de tanques por nivel
# 3. Con un for recorremos todas las llaves y en el if si esta llave coincide con la que el usuario
# ingreso se imprime un mensaje y despues entra en otro for para recorrer los valores dentro de la lista.

searchTank: str = input('¿Que nivel de tanques estas buscando? ')

mi_diccionario: dict = {
    'VII': ['T-34', 'Tiger'],
    'IX': ['E-75', 'Emil'],
    'X': ['E-100', 'IS-4']
}

for llave in mi_diccionario.keys():
    if searchTank == llave:
        print('El nivel es: ' + searchTank)
        for tanque in mi_diccionario[llave]:  # Accede a los valores de la llave que hizo match de la entrada del usuario
            print(tanque)



