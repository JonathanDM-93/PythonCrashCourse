# TRY IT YOURSELF pag. 154 8-12 Sandwiches
# Escribe una función que acepte una lista de elementos de personas que quieren un sandwich. La función debe tener un
# parametro que recolecte todos los elementos que se ingresen y debe imprimir el resumen de los sanwiches que se
# ordenaron.

def make_sandwich(person_name, *ingredientes):
    print(f"El cliente: {person_name.upper()} quiere un sandwich con los siguientes ingredientes: ")
    for ingrediente in ingredientes:
        print(f"- {ingrediente}")


make_sandwich('Jonathan', 'Jamon', 'Jitomante', 'Lechuga', 'Queso')
# El cliente: JONATHAN quiere un sandwich con los siguientes ingredientes:
# - Jamon
# - Jitomante
# - Lechuga
# - Queso

print("\n[*]\n")

# TRY IT YOURSELF pag. 154 8-13 User Profile
# Copia la función que se hizo en el ejercicio user_profile.py y agrega tres pares llave-valor que te describen

import pandas as pd


def build_user(first_name, last_name, **user_info):
    """Construye un diccionario que contenga todo lo que conocemos del usuario"""
    # El valor que se pasa en el argumento se almacena en la llave del diccionario
    profile: dict = {'first_name': first_name,
                     'last_name': last_name}
    # Se declara en la función la llave y el valor que se almacenaran en el diccionario
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_user('Jonathan', 'Maldonado', pais='Ucrania', estudios='Doctor',
                          mascota='Perro', deporte='Tenis', altura=1.70)
print(user_profile)

print("\n[*]\n")

# Lo convertí a un Dataframe de pandas
passDataFrame = pd.DataFrame([user_profile])
print(passDataFrame)

print("\n\n[*]\n\n")


# TRY IT YOURSELF pag. 154 8-14 Cars
# Escribe una función que almacene información sobre un automóvil dentro de un diccionario. La función debera recibir
# siempre el nombre del creador y el nombre del modelo. La función debe de aceptar un número arbitrario de argumentos.

def create_car(marca, modelo_auto, **caracteristicas_auto):
    """Crear el diccionario"""
    theCar = {'Marca': marca,
              'Modelo_Auto': modelo_auto}
    for key, value in caracteristicas_auto.items():
        theCar[key] = value
    return theCar


custom_car = create_car('Ford', 'Aveo', color='Gris', año='2023')
print(custom_car)
# {'Marca': 'Ford', 'Modelo_Auto': 'Aveo', 'color': 'Gris', 'año': '2023'}
