# Ejemplos del TRY IT YOURSELF PÁGINA 102
# Diccionarios nos permiten relacionar objetos a un valor en específico (no necesariamente numérico).
# Creemos un ejemplo sencillo.

TipoTanque: dict = {'Tanque': 'Tiger', 'Velocidad': '35'}
# Lo que describimos aqui es el tipo de tanque y su velocidad (km/hr) promedio.
# Para acceder al valor asociado a la llave en un print podemos llamar a la llave ('Key')
print(TipoTanque['Tanque'], TipoTanque['Velocidad'])
# >> Tiger 35
# Se imprime el valor de la Key 'Tanque' y el valor de la Key 'Velocidad'.

# Supongamos que queremos añadir otra Key-value al diccionario

TipoTanque['Blindaje'] = 262
TipoTanque['Penetración'] = 250
print(TipoTanque)
# {'Tanque': 'Tiger', 'Velocidad': '35', 'Blindaje': 262, 'Penetración': 250}
# Observamos que se agregaron nuevas Key-Value al diccionario.

print('\n[*]\n')

# Creemos un diccionario nuevo para ver como podemos cambiar un valor dentro del diccionario
TanquePosicion: dict = {'Tanque': 'T-34', 'Velocidad': '100'}
print('Velocidad incorrecta:' + TanquePosicion['Velocidad'])
# Queremos cambiar la velocidad que es incorrecta de 100 km/hr
TanquePosicion['Velocidad'] = '45'
print('Velocidad correcta:' + TanquePosicion['Velocidad'])

print('\n[*]\n')

# Ahora vamos a jugar con nuestros tanques
# Imaginemos que nuestro tanque se posiciona en un plano cuadriculado para seguir su movimiento
# Y podemos desplazarnos un cuadro o más a la vez de acuerdo a la velocidad que presente nuestro
# tanque ('Baja' , 'Intermedia' , 'Alta')

TanqueVel: dict = {'Tanque': 'T-34', 'Velocidad': 'Intermedia', 'Posicion_x': 0, 'Posicion_y': 1}
# Imprimamos la posición original del tanque
print('Posición Original en x: ' + str(TanqueVel['Posicion_x']))
print('Posición Original en y: ' + str(TanqueVel['Posicion_y']))

print('\n[*]\n')

# Si tiene una Velocidad Baja se movera 1 cuadro, Intermedia 2 cuadros, Alta 3 cuadros
# Por facilidad digamos que nuestro tanque se movera a la derecha

if TanqueVel['Velocidad'] == 'Baja':
    incremento_x = 1
elif TanqueVel['Velocidad'] == 'Intermedia':
    incremento_x = 2
else:
    # El ultimo es vel Alta
    incremento_x = 3

# La nueva posición del tanque es:
TanqueVel['Posicion_x'] = TanqueVel['Posicion_x'] + incremento_x
print('Nueva posición: ' + str(TanqueVel['Posicion_x']))
# Vemos que el tanque tiene una velocidad intermedia asi que solo aumenta en 2 la posicion en x
