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

print('\n[*]\n')

# EJEMPLO 5
# También podemos usar el metodo keys() para buscar a una persona o Llave en este caso dentro
# del diccionario

# Creemos un diccionario para ejemplificar lo anterior. Este diccionario tiene como llave los nombres
# y en su valor indicando que están presentes dentro del mismo.
ingresaNombre: str = input('Ingresa el nombre que buscas: ')

testDiccionario: dict = {
    'Jonathan': 'Presente[1]',
    'Karla': 'Presente[2]',
    'Charles': 'Presente[3]',
    'Magnolia': 'Presente[4]'
}

if ingresaNombre not in testDiccionario.keys():
    print('Este nombre no esta en el diccionario')
else:
    print('Este nombre si esta en el diccionario ')

# Lo interesante de este ejemplo es que cuando se entra en la parte del if busca en automatico
# si la llave coincide con lo que ingreso el usuario sin la necesidad de un for.

print('\n[*]\n')

# EJEMPLO 6
# Recorriendo un Diccionario en Orden
# Supongamos que queremos ordenar un diccionario donde los usuarios ingresaron sus nombres de forma
# aleatoria, esto quiere decir que los devolveremos en orden alfabetico

NombresAleatorios: dict = {
    'Kevin': 11,
    'Ana': 1,
    'Sofia': 20,
    'Bianca': 2,
    'Dante': 4,
    'Lourdes': 12,
}
for nombres, numero in sorted(NombresAleatorios.items()):
    print(nombres + ' posición ' + str(numero))

# >>
# Ana posición 1
# Bianca posición 2
# Dante posición 4
# Kevin posición 11
# Lourdes posición 12
# Sofia posición 20

# Vemos que imprime en orden los nombres.

print('\n[*]\n')

# EJEMPLO 7
# Recorriendo un diccionario a traves de sus valores
# Si en este caso ahora estamos enfocados en los valores del diccionario, podemos acceder
# a ellos a traves del método values().
# Creemos un diccionario con los costos ficticios de algunos celulares:

CelPrecio: dict = {
    'Iphone': 18000,
    'Samsung': 12500,
    'Xiaomi': 7950,
    'Nokia': 7699,
}
for precio in CelPrecio.values():
    print('El precio de los equipos son: ' + str(precio))
