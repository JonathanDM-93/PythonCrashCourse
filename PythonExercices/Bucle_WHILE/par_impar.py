# En este nuevo tema aborda un operador interesante que es el OPERADOR MODULO ó %
# Este operador devuelve el residuo de una división
# Comencemos un algo sencillo
SimpleDiv = 31 / 12
print(SimpleDiv)
# >> 2.5833333333333335
print(type(SimpleDiv))
# Vemos que en la división normal se devuelve el valor de la division con el residuo y es la
# variable es de tipo flotante

# Apliquemos el operador %
SimpleDiv = 31 % 12
print(SimpleDiv)
# >> 7
print(type(SimpleDiv))
# Vemos que devuelve el residuo y es de tipo entero

# Hagamos un pequeño programa donde un usuario ingrese un número y le diga al usuario
# si el número es par o impar

enter: float = float(input('Ingresa el número que quieras: '))

if enter % 2 == 0:  # Lo que indica es que si no hay residuo es PAR
    print('El número es par.')
else:
    print('El número es impar.')  # Si hay residuo se ejecuta el else
