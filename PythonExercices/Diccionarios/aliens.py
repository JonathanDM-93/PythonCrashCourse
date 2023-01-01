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
aliens: list = []

for numero_alien in range(30):
    nuevo_alien: dict = {
        'color': 'verde',
        'puntos': 5,
        'velocidad': 'baja',
    }
    aliens.append(nuevo_alien)

# Imprime los primeros 5 elementos
for five_elements in aliens[0:5]:
    print(five_elements)
print('...')

# Mostrar cuentos aliens hemos creado:
print('Número total de aliens: ' + str(len(aliens)))

# >>
# Número total de aliens: 30
