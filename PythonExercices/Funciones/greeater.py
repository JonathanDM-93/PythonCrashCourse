# Usando una función con in loop while

def get_formatted_name(first_name, last_name):
    """Regresa el nombre completo"""
    full_name = first_name + ' ' + last_name
    return full_name.title()


while True:
    print("\nIngresa tu nombre: ")
    print("(enter 'quit' en cualquier momento para salir")

    theName: str = input("Ingresa tu nombre: ")
    if theName == 'quit':
        break

    lastName: str = input("Ingresa tu apellido: ")
    if lastName == 'quit':
        break

    formattedName: str = get_formatted_name(theName, lastName)
    print(f"\n Hola, {formattedName}")
