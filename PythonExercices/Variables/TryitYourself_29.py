# TRY IT YOURSELF pag 29 Strings

# Un string simplemente es una serie de caracteres y en python deben iniciar y terminar en comillas

my_String = "Esto es un String en Python"
print(my_String)  # (1)

# Cambiando un String con Métodos
# Existen métodos que son acciones en Python que permiten cambiar o alterar los datos

'''Métodos
 .title
 .upper
 .lower
por mencionar algunos.'''

print(my_String.upper())  # (2)
print(my_String.lower())  # (3)
print(my_String.capitalize())  # (4)

'''
Esto es un String en Python # (1)
ESTO ES UN STRING EN PYTHON # (2)
esto es un string en python # (3)
Esto es un string en python # (4)
'''
# +++++++++++++++++++++++++++ DELIMITADOR +++++++++++++++++++++++ #

# Combinando o concatenando strings
my_wordOne = "Este es un mensaje para"
my_wordTwo = "mi yo del futuro cuando vuelva a leer este mensaje"
my_wordThree = "sera un experto en Python."

oracion = my_wordOne + " " + my_wordTwo + " " + my_wordThree
print(oracion)  # (5)
''' Este es un mensaje para mi yo del futuro cuando vuelva a leer este mensaje sera un experto en Python. # (5)'''
# +++++++++++++++++++++++++++ DELIMITADOR +++++++++++++++++++++++ #

# Remover espacios en Blanco
'''Para esto podemos utilizar los sig. métodos:
.rstrip() -> quita los espacios a la derecha
.lstrip() -> quita los espacios a la izquierda
.strip() -> quita todos los espacios en blanco'''

whitespaceWord = " Python "
print(whitespaceWord.rstrip())  # (6)
print(whitespaceWord.lstrip())  # (7)
print(whitespaceWord.strip())   # (8)

'''
Python_  # (6)
_Python  # (7)
Python   # (8)
'''
