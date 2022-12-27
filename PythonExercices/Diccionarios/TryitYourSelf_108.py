# TRY IT YOURSELF PÁGINA 108
# Recordemos que los diccionarios pueden almacenar una cantidad enorme de datos
# de varias formas. Existen también varias maneras de recorrer los diccionarios
# a traves de sus llaves-valor, o individualmente ya sea con las llaves o los valores.
# Creemos un diccionario que diseñado para almacenar información sobre un usuario:

UsuarioPrimario: dict = {
    'Nombre': 'Jonathan',
    'Apellido': 'Lopez',
    'Edad': '30',
}
# Hasta el momento conocemos que podemos acceder al valor utilizando la llave asociada al mismo.
# print(UsuarioPrimario['Nombre'])
# >> Jonathan

# Pero si quisiéremos ver el diccionario completo hacemos lo siguiente:
for key, value in UsuarioPrimario.items():
    print('LLave: ' + key)
    print('Valor: ' + value)

# >>
# LLave: Nombre
# Valor: Jonathan
# LLave: Apellido
# Valor: Lopez
# LLave: Edad
# Valor: 30

# Vemos que se imprime el diccionario. Agregamos el método items() después del nombre del
# diccionario para que no retorne los pares Llave-Valor.

print('\n[*]\n')

# Veamos otro ejemplo de recorrer diccionarios:

lenguajes_favoritos: dict = {
    'Jonathan': 'Python',
    'Karen': 'C++',
    'Arnold': 'JAVA',
    'Jenny': 'Pearl',
}

for nombre, lenguajes in lenguajes_favoritos.items():
    print('El lenguaje favorito de ' + nombre + ' es ' + lenguajes + '!')

# >>
# El lenguaje favorito de Jonathan es Python!
# El lenguaje favorito de Karen es C++!
# El lenguaje favorito de Arnold es JAVA!
# El lenguaje favorito de Jenny es Pearl!

# Observamos que podemos agregar nombres descriptivos a los pares Llave-Valor para que sean mas
# descriptivos y sea más entendible nuestro codigo.

print('\n[*]\n')

# Recorriendo un diccionario a traves de sus Llaves.
# El método keys() es util si solo queremos imprimir las llaves sin la necesidad de traer los valores
# asociados a ellas. Utilicemos el mismo diccionario de los lenguajes_favoritos:

for name in lenguajes_favoritos.keys():
    print('Los nombres son: ' + name)

# >>
# Los nombres son: Jonathan
# Los nombres son: Karen
# Los nombres son: Arnold
# Los nombres son: Jenny

# Observamos que al utilizar el método keys() solo nos devuelve las Llaves del diccionario.

print('\n[*]\n')

# EJEMPLO 4
# Hagamos otro ejemplo utilizando el mismo diccionario de:
lenguajes_favoritos: dict = {
     'Jonathan': 'Python',
     'Karen': 'C++',
     'Arnold': 'JAVA',
     'Jenny': 'Pearl',
 }

# Creemos una lista:
ListaNombres: list = ['Jonathan', 'Jenny']
for nombres in lenguajes_favoritos.keys():
    print(nombres)

    if nombres in ListaNombres:
        print('Hola ' + nombres + ' veo que tu lenguaje favorito es ' + lenguajes_favoritos[nombres] + '!')

# Lo que sucede en este ejemplo es:
# 1.- Se creo un diccionario.
# 2.- Se creo una lista con algunos nombres que también se encuentran dentro del diccionario.
# 3.- En el for se recorrera el diccionario a traves de sus LAVES y se imprimirán los nombres
# 4.- Vemos que el if esta identado al nivel del for, entonces se recorrera también la lista
# ListaNombres, por lo que si dentro de esta lista se encuentra una coincidencia con las LLAVES
# del diccionario se imprime un mensaje específico dentro del if.

# >>
# Jonathan
# Hola Jonathan veo que tu lenguaje favorito es Python!
# Karen
# Arnold
# Jenny
# Hola Jenny veo que tu lenguaje favorito es Pearl!
