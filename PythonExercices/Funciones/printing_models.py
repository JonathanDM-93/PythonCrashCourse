# Modificando una lista en una función
# Cuando pasas una lista a una función, la función puede modificar la lista. Cualquier cambio realizado a la lista
# dentro del cuerpo de la función es permanente permitiendo hacer un trabajo más eficiente cuando trabajas con grandes
# conjuntos de datos.
"""
# Empieza con algunos diseños que necesitan ser impresos
unprinted_designs: list = ['iphone_case', 'robot pendant', 'dodecahedron']
completed_models: list = []

# Simula que se está imprimiendo cada diseño, hasta qye no quede ninguno
while unprinted_designs:
    # Quitar cada uno del elemento de la lista y almacenarlos en 'current_design'
    current_design = unprinted_designs.pop()

    # Simula que estás creando la impresión 3D del diseño
    print(f"Imprimiendo modelo: {current_design}")
    completed_models.append(current_design)

# Imprime todos los modelos completados
print(f"\nLos siguientes modelos han sido impresos: ")
for i in completed_models:
    print(i)
"""

print('\n[*]\n')


# Organizaremos el código anterior escribiendo dos funciones que ejecutaran una solo actividad.

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simula que estás creando la impresión 3D del diseño
        print(f"Imprimiendo modelo: {current_design}")
        completed_models.append(current_design)


def show_completed_models(completed_models):
    # Imprime todos los modelos completados
    print(f"\nLos siguientes modelos han sido impresos: ")
    for completed_model in completed_models:
        print(completed_model)


# Declarar las listas
unprinted_designs: list = ['iphone_case', 'robot pendant', 'dodecahedron']
completed_models: list = []

# Llamar a las funciones
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
