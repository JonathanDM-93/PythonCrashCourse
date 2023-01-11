# Hacer los ejercicios del TRY IT YOURSELF PAG 114.

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


# EJE# EJERCICIO 6-8 Pets