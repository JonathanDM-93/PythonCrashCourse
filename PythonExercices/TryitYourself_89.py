# TRY IT YOURSELF pág. 89
# En esta sección daremos continuidad al tema del condicional IF
# Hay que tener en cuenta que la identación juega un papel importante cuando
# se esta ejecutando un bloque todo lo que se encuentre dentro del bloque se
# ejecutara si la condición resulta verdadera.

smartPhone: str = 'Iphone'
if smartPhone == 'Iphone':
    print('Tienes un ' + smartPhone + ' asombroso!')
    print('Yo quisiera uno también.')
# Sin embargo, si el telefono no fuera Iphone el bloque no generaría respuesta y por eso
# entraremos a la parte de las declaraciones if-else

print('\n[*]\n')

# Declaraciones if-else
edadUsuario: str = input('Ingresa tu edad: ')
if edadUsuario >= str(18):
    print('Eres mayor de edad puedes pasar.')
else:
    print('Eres menor de edad no puedes pasar.')

# Si eres mayor de edad puedes pasar, si no la entrada es prohibida para ti.

print('\n[*]\n')

# Cadena de if-elif-else
# Podemos usar este tipo de bloques para evaluar un mayor tipo de condiciones

# Imagina que queremos comprobar la edad y de acuerdo con ello se te cobrara
# el tipo de entrada en el cine
print('El costo de las entradas son: \n')
print('Mayores de 18 años $ 80.00 \n')
print('Menores 18 años $ 55.00 \n')
print('Menores a 5 años gratis \n')

edadTicket: str = input('Ingresa tu edad para saber que tipo de boleto necesitas: ')
edadTicket: int = int(edadTicket)
if edadTicket < 4:
    print('Entrada gratis')
elif edadTicket <= 17:
    print('Boleto de $ 55.00')
else:
    print('Boleto de $ 80.00')

print('\n[*]\n')

# En el ejemplo anterior podemos hacer unas modificaciones para que sea un poco más claro
# Quitaremos el else que en este caso no es necesario

print('** Mejoramiento del ejemplo anterior **\n')
print('El costo de las entradas son: \n')
print('Mayores de 18 años $ 80.00 \n')
print('Menores 18 años $ 55.00 \n')
print('Menores a 5 años gratis \n')

edadTicket: str = input('Ingresa tu edad para saber que tipo de boleto necesitas: ')
edadTicket: int = int(edadTicket)
if edadTicket <= 4:
    valorTicket: int = 0
    print('El costo de tu boleto es: $ ' + str(valorTicket))
elif edadTicket in range(5, 17):
    valorTicket: int = 55
    print('El costo de tu boleto es: $ ' + str(valorTicket))
elif edadTicket >= 18:
    valorTicket: int = 80
    print('El costo de tu boleto es: $ ' + str(valorTicket))

print('\n[*]\n')

# Bueno aqui vemos que parece que funciona mejor ya colocamos un condicional para
# los niños que tienen <= 4 años pasen gratis. Las personas de 5 años a 17 pagan 55
# y finalmente las personas con más de 18 años pagan boleto de adulto.

# En el anterior ejemplo vemos que esta cadena de if-elif-else es un muy util; sin embargo,
# solo es apropiado si cuando lo usamos solo necesitamos que alguna de las condiciones se cumpla.
# Pero en ocasiones es necesario que todas las condiciones que se encuentran en nuestro programa sean
# verificadas, en este caso únicamente deberíamos utilizar una serie de if consecutivos.

someList: list = ['item1', 'item2']
if 'item1' in someList:
    print('El item1 si esta en la lista.')
if 'item2' in someList:
    print('El item2 esta en la lista.')
if 'item3' in someList:
    print('El item3 si esta la lista')
if 'item4' in someList:
    print('El item3 si esta la lista')

# Las respuestas que se imprimen son:

# El item1 si está en la lista.
# El item2 está en la lista.

# Como vemos el programa pasa por cada if e imprime el texto si la condición es verdadera.
