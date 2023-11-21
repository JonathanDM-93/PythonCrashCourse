# Usando argumentos llave-valor arbitrarios
# Algunas ocasiones necesitarás que tus funciones acepten un número arbitrario de argumentos, pero no sabras de primera
# mano que tipo de información se pasara a la función. En este caso, tendrás que escribir funciones que acepten
# par llave-valor como la llamada de la declaración lo solicite.
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


user_profile = build_user('Jonathan', 'Maldonado', pais='Ucrania', estudios='Doctor', mascota='Perro')
print(user_profile)
# {'first_name': 'Jonathan', 'last_name': 'Maldonado', 'pais': 'Ucrania', 'estudios': 'Doctor', 'mascota': 'Perro'}

print("\n[*]\n")

# Decidí verlo en un dataframe de pandas
dataframe_UP = pd.DataFrame([user_profile])
print(dataframe_UP)

#   first_name  last_name     pais estudios mascota
# 0   Jonathan  Maldonado  Ucrania   Doctor   Perro
