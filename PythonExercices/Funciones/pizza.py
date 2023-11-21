# Pasando un número arbitrario de argumentos.
# A veces uno no tiene el tiempo para delimitar cuantos argumentos necesita aceptar una función. Python permite a una
# función obtener un número arbitrario de argumentos desde la llamada de la declaración.

# Observemos la siguiente función, donde tiene un solo parametro, *toppings, pero este parametro recolecta tantos
# argumentos como la linea los provee.

def make_pizza(*toppings):
    """Imprime la lista de toppings que han sido solicitados"""
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('champiniones', 'piña', 'extra queso')

# ('pepperoni',)
# ('champiniones', 'piña', 'extra queso')

# Versión 2 de la función
# - pepperoni
# - champiniones
# - piña
# - extra queso

# El asterisco en el nombre del argumento le dice a python hacer un tupla vacía y almacenar cualquier valor que se
# reciba dentro de esta tupla.

print("\n[*]\n")


# Combinando argumentos de posición y arbitrarios
# En este caso se tiene que colocar el argumento que acepta varios parámetros al ultimo de la definición de la función.

# Digamos que queremos hacer un hotdog, y el primer parametro se define el tamaño y por ultimo los complementos.

def make_hot_dog(size, *complementos):
    """Crear un hotdog de cierto tamaño con complementos"""
    longitud: int = int(size)
    print(f"Crea un hotdog de tamaño (cm): {longitud}")

    # El for imprime cada uno de los elementos provenientes del argumento *complementos
    for complemento in complementos:
        print(complemento)


make_hot_dog(12, 'jitomate', 'tocino', 'mostaza')
