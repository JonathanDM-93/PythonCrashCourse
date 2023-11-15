# Modificando una lista en una función
# Cuando pasas una lista a una función, la función puede modificar la lista. Cualquier cambio realizado a la lista
# dentro del cuerpo de la función es permanente permitiendo hacer un trabajo más eficiente cuando trabajas con grandes
# conjuntos de datos.

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

print('\n[*]\n')

