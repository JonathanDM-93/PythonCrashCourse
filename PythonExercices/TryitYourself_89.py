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
