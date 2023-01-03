# En esta seccion abordaremos el tema de NESTING (Aninado)
# En ciertos contextos necesitaremos guardar un grupo de diccionarios en una lista
# o viceversa guardar una serie de caracteristicas como valores en un diccionario.
# A lo anterior se le llama Nesting. Esto significa que podremos anidar un conjunto
# de diccionarios en una lista, una lista de caracteristicas de una lista dentro de
# un diccionario o también diccionarios dentro de otros diccionarios.

# En esta ocasión seguiremos a pie de página el ejemplo del libro.

# Crearemos 3 diccionarios:
alien_0: dict = {
    'color': 'verde',
    'puntos': 5,
}

alien_1: dict = {
    'color': 'amarillo',
    'puntos': 10,
}

alien_2: dict = {
    'color': 'rojo',
    'puntos': 15,
}

aliens: list = [alien_0, alien_1, alien_2]  # Guardar los diccionarios en una lista
for items in aliens:
    print(items)

# >>
# {'color': 'verde', 'puntos': 5}
# {'color': 'amarillo', 'puntos': 10}
# {'color': 'rojo', 'puntos': 15}

print('\n[*]\n')

# Observamos que el nombre que les dimos a las variables en los diccionarios pueden ser almacenadas
# en una lista.

# Creemos una serie de aliens con las siguientes líneas:

# Crear una lista vacía:
ListAliens: list = []

for add_alien in range(30):
    green_alien: dict = {
        'color': 'verde',
        'puntos': 5,
        'velocidad': 'baja',
    }
    ListAliens.append(green_alien)

# Queremos ahora cambiar el color de los tres primeros aliens, a traves de un for:
for color_alien in ListAliens[0:3]:
    if color_alien['color'] == 'verde':  # Si la clave del color del alien es verde cambiara
        color_alien['color'] = 'amarillo'
        color_alien['velocidad'] = 'intermedio'
        color_alien['puntos'] = '10'
    elif color_alien['color'] == 'amarillo':  # Agregamos un bloque elif que cambia los alies a color rojo
        color_alien['color'] = 'rojo'
        color_alien['velocidad'] = 'alta'
        color_alien['puntos'] = '15'


# Imprime los primeros 5 elementos
for five_elements in ListAliens[0:5]:
    print(five_elements)
print('...')

# Mostrar cuentos aliens hemos creado:
print('Número total de aliens: ' + str(len(ListAliens)))

# >>
# Número total de aliens: 30
