# Passing Arguments
# Una función puede tener multiples parametros, una llamada a una función pude necesitar multiples parametros.
# Podemos usar "argumentos de posición" los cuales se necesitan usar en el mismo orden en el cual fueron escritos.
# Por otro lado "argumentos llave" donde cada argumento consiste en una variable llamada valor y listas y diccionarios
# de valores.

"""Argumentos de posición"""


def describe_pets(tipo_mascota, nombre_mascota):
    n = 0
    while n < 1:
        print(f"Yo tengo un {tipo_mascota}")
        print(f"Mi {tipo_mascota} tiene el nombre de {nombre_mascota}")
        n += 1


def pets_default(mascota_nombre, mascota_tipo="Gato"):
    # Lo interesante es que no puede ir antes un parametro default de un parametro no default
    print(f"{mascota_tipo}")
    print(f"{mascota_nombre}")


if __name__ == "__main__":
    # Preguntar a un usuario.
    # clase_pet = input(str("¿Que tipo de mascota tienes?"))
    # nombre_pet = input(str("¿Cual es su nombre?"))
    tipo = "Perro"
    nombre = "Drax"

    # Llamar a la función
    # Vemos que colocamos los argumentos en orden
    describe_pets(tipo, nombre)
    # Yo tengo un Perro
    # Mi Perro tiene el nombre de Drax

# -------------------------------------------------------------------------------------------------------------------- #
# En el siguiente ejemplo vemos que ahora utilizamos "Keyword Arguments"
# Asignamos nuevos valores, y al momento de llamar a la función ingresamos en los parametros en nombre que declaramos
# el primer argumento en la función y hacemos lo mismo con el segundo argumento.
    print('\n')
    tipo_2: str = "Gato"
    nombre_2: str = "Pelusa"

    describe_pets(tipo_mascota=tipo_2, nombre_mascota=nombre_2)
    # Yo tengo un Gato
    # Mi Gato tiene el nombre de Pelusa

    print('\n')
# Para asignar valores default ver la funcion pets_default ya vemos que no es necesario agregar en la función el
# argumento del tipo de mascota porque ya será Gato cada vez que se llame a esta función
    pets_default(mascota_nombre="Terry")
    # Gato
    # Terry
