# Hacer los ejercicios del TRY IT YOURSELF PAG 114.
import random

# EJERCICIO 6-7 People
# Hacer tres diccionarios con información sobre ellos y guardar los diccionarios en una lista,
# y recorres la lista a traves de un loop. Imprime todo lo relacionado con esa persona.
# Se esta retomando el tema de NESTING

person_1: dict = {
    'first_name': 'Katia',
    'last_name': 'Peralta',
    'age': 26,
    'city': 'New York',
}

person_2: dict = {
    'first_name': 'Kevin',
    'last_name': 'White',
    'age': 48,
    'city': 'México',
}

person_3: dict = {
    'first_name': 'Magnolia',
    'last_name': 'Williams',
    'age': 27,
    'city': 'Atlanta',
}

people: list = [person_1, person_2, person_3]
for person in people:
    print(person)

# >> Imprime todas las Llaves-Valor de cada persona

# {'first_name': 'Katia', 'last_name': 'Peralta', 'age': 26, 'city': 'New York'}
# {'first_name': 'Kevin', 'last_name': 'White', 'age': 48, 'city': 'México'}
# {'first_name': 'Magnolia', 'last_name': 'Williams', 'age': 27, 'city': 'Atlanta'}

print('\n[*]\n')

# EJERCICIO 6-8 Pets
# 1.- Crear varios diccionarios, donde el nombre de cada diccionario es el nombre de una mascota
# 2.- En cada diccionario incluye el tipo de animal y el nombre del dueño.
# 3.- Recorre la lista de los diccionarios a traves de un loop e imprime todo sobre la mascota.

Draks: dict = {
    'Tipo': 'Perro',
    'Raza': 'Husky',
    'Dueño': 'Edwin',
}

Luke: dict = {
    'Tipo': 'Perro',
    'Raza': 'Pastor Inglés',
    'Dueño': 'Miguel',
}

namePets: list = [Draks, Luke]
for name in namePets:
    print(name)

print('\n[*]\n')

# EJEMPLO 6-9 Favorite Places
# 1.- Crea un diccionario llamado favorite_places, piensa en tres lugares para que sirvan como KEYS
# y guarda para cada lugar una persona.
# 2.- recorre cada diccionario e imprime el nombre de la persona con su sitio favorito.

favorite_places: dict = {
    'Cancún': 'Jonathan',
    'Mazatlán': 'Gina',
    'Acapulco': 'Enrique',
    'Teotihuacan': 'Kevin',
}

for places, names in favorite_places.items():
    print(names + ' ama visitar ' + places)
# >>
# Jonathan ama visitar Cancún
# Gina ama visitar Mazatlán
# Enrique ama visitar Acapulco
# Kevin ama visitar Teotihuacan

print('\n[*]\n')

# EJEMPLO 6-10 Favorite numbers
# 1.- Asigna a varias personas como Llaves
# Y agrega algunos de sus numeros favoritos como sus Valores
# Imprime los nombres y sus numeros favoritos a traves de un loop

favorite_num: dict = {
    'Wilson': [7, 36, 200],
    'Lilia': [1, 48, 789],
}

for name, numeros in favorite_num.items():
    print('Los números favoritos de ' + name + ' son: ')
    for num in numeros: # Recorre cada número individualmente
        print('\t' + str(num))

# >>
# Los números favoritos de Wilson son: [7, 36, 200]
# Los números favoritos de Lilia son: [1, 48, 789]

