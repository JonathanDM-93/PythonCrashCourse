# RETORNA UN SIMPLE VALOR página 142.
# Una función no siempre tiene que desplegar directamente una salida, en cambio,
# puede procesar cierta información y entonces retornar un valor o conjunto de valores.
# Toma el nombre y apellido y regresa el nombre completo formateado

def get_formatted_name(first_name, last_name):
    """Regresa el nombre completo"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


# Nota: Cuando llamas una función que retorna un valor, necesitas crear una variable donde el valor que se retorna
# pueda ser almacenado.
# En el ejemplo el valor que se retorna se almacena en la variable 'musico'

# Crear una variable llamada 'musico' y llamar a la función
musico = get_formatted_name("Jonathan", "Maldonado")
print(musico)
# Jonathan Maldonado
