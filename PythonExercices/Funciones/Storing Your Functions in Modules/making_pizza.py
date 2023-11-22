# Crearemos el archivo making_pizza en un archivo diferente pero dentro del mismo directorio que pizza.py
# Importamos el módulo de pizza y haremos dos llamadas

import pizza

# LLamar al módulo - llamar a la función a traves del operador punto [.] e ingresar los argumentos
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(20, 'piña', 'queso', 'chiles')


# Esta es la primera aproximación para importar, en la cuál tu simplemente escribes 'import' seguido del nombre
# del módulo, hace que cualquier función desde el módulo sea disponible dentro de tu programa. Si tú usas este tipo de
# declaración para importar el módulo 'module_name.py cada función en el módulo está disponible a traves de la siguiente
# sintaxis:
"""module_name.function_name()"""
