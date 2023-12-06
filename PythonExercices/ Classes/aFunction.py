# Algunos conceptos que deben estar claros al crear una función
# Definamos una simple función

def oneFunction(parameter_One, parameter_Two):
    """La función toma dos parametros"""
    calculate = parameter_One * parameter_Two
    print(calculate)
    return calculate


# Llamar a la función

enter_One: int = 30
enter_Two: int = 5

result_function = oneFunction(enter_One, enter_Two)

# Vemos que en la declaración de la función se asignan los parametros que debe tener la funció.
# En el cuerpo de la función vemos que toma los parametros y hace una multiplicación
# Finalmente declaramos algunas variables que serán pasados a la función y hara el cálculo e imprimir el resultado.
