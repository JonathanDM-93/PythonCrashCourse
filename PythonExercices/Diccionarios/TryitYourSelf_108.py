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

# >> LLave: Nombre
# Valor: Jonathan
# LLave: Apellido
# Valor: Lopez
# LLave: Edad
# Valor: 30

# Vemos que se imprime el diccionario. Agregamos el método items() después del nombre del
# diccionario para que no retorne los pares Llave-Valor.

