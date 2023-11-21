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

