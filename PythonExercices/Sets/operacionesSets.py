# Abordaremos las operaciones con los Sets

# Union entre conjuntos usamos el método .union()
set_A: set = {'MEX', 'COL', 'BOL'}
set_B: set = {'BOL', 'AR', 'COL'}

set_union: set = set_A.union(set_B)
# print(set_union)
# >> {'MEX', 'BOL', 'AR', 'COL', 'PE'}
# Vemos la unión de los conjuntos sin duplicar.

# También la union la podemos hacer a traves de operadores |
unionOperador: set = (set_A | set_B)
# print(unionOperador)
# >> {'MEX', 'BOL', 'AR', 'COL', 'PE'}

# Intersección de conjuntos se verá ahora que elementos se comparten entre conjuntos.
set_interseccion: set = set_A.intersection(set_B)
# print(set_interseccion)
# >> {'COL'}

interseccionOperador: set = (set_A & set_B)
# print(interseccionOperador)
# >> {'COL'}

# Diferencia entre conjuntos.
set_diff: set = set_A.difference(set_B)
# print(set_diff)
# >> {'MEX'}

diffOperador: set = (set_A - set_B)
# print(diffOperador)
# >> {'MEX'}

# set_A: set = {'MEX', 'COL', 'BOL'}
# set_B: set = {'BOL', 'AR', 'COL'}
# Como solo comparten a Bolivia es el unico valor que se quitara.

# Diferencia simétrica entre conjuntos
# Hace la unión con los elementos que se tiene en comun y devulve los elementos
# que no tienen en común los Set´s.

set_diffAsimetrica: set = set_A.symmetric_difference(set_B)
# print(set_diffAsimetrica)
# >> {'AR', 'MEX'}

diffAasimetricaOperador: set = (set_A ^ set_B)
# print(diffAasimetricaOperador)
# >> {'AR', 'MEX'}



