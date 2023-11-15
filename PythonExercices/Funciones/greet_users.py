# Pasando una lista página 147
# Encontraras que es util pasar una lista a una función, cuando pasas una lista a una función tiene acceso directo
# a su contenido de la lista.

def greet_users(names_list):
    for names in names_list:
        msg: str = f"Hola {names}!".title()
        print(msg)


# Declarar una lista con nombres
user_names: list = ['Jonathan', 'Abigail', 'Marcos']

# Llamar a la función
greet_users(user_names)

# Hola Jonathan!
# Hola Abigail!
# Hola Marcos!



