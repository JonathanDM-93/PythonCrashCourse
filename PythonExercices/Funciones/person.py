# Retornando un diccionario
# Una función puede retornar cualquier tipo de valor que necesites, incluyendo complejas estructuras de datos como:
# listas y diccionarios. El siguiente ejemplo de función toma en partes el nombre y regresa un diccionario que represe-
# senta una persona.

def build_person(first_name, last_name):
    person: dict = {'first': first_name,
                    'last': last_name, }
    return person


# Declarar la variable donde se almacenara el resultado de la función
musician = build_person('Jonathan', 'Perez')

print(musician)


# Una segunda versión de la función donde acepte la edad de la persona

def build_person_age(first_name, last_name, age=''):
    person: dict = {'first': first_name,
                    'last': last_name, }
    if age:
        person['age'] = age
    return person


# Al final agregué una cast a string, ya que acepta un string desde la función.
musico = build_person_age('Santiago', 'Hernandez', str(35))
print(musico)
