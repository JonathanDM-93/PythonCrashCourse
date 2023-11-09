# Hacer que un arguemnto sea opcional
# Algunas ocasiones tiene sentido hacer que un argumento sea opcional para que algunas personas cuando usen la función
# puedan elegir proveer información extra si asi lo requieren.

def get_formatted_name(first_name, middle_name, last_name):
    full_name: str = f"{first_name}{' '}{middle_name}{' '}{last_name}"
    return full_name.title()


ingresaPrimerNombre: str = "Jonathan"
ingresaSegundoNombre: str = "Jose"
ingresaApellido: str = "Maldonado"

# Observamos que la función necesita de tres argumentos para funcionar.
musico = get_formatted_name(ingresaPrimerNombre, ingresaSegundoNombre, ingresaApellido)
print(f"Tu nombre es: {musico}")


# Sin embargo, en ocasiones no se necesita el segundo nombre, pero la anterior función necesita tres argumentos, para
# hacer el segundo nombre sea opcional daremos a 'middle_mame' un argumento vacío como default y se ignorara
# hasta que el usuario asigne algún valor.

# Creemos la función

def get_formatted_middle(first_name, last_name, middle_name=''):
    if middle_name:
        full_name: str = f"{first_name}{' '}{middle_name}{' '}{last_name}"
        return full_name.title()
    else:
        full_name: str = f"{first_name}{' '}{last_name}"
        return full_name.title()


name = "Jonathan"
secondName = "Kevin"
lastName = "Gutierrez"

# Con los tres argumentos
# Llamar a la función
name_musician = get_formatted_middle(name, secondName, lastName)
print(name_musician)

# Con dos argumentos
name = "Eduardo"
secondName = "Fernandez"
# Llamar a la función
name_musician = get_formatted_middle(name, lastName)
print(name_musician)


