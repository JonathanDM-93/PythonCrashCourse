# Este juego lo escribiremos paso a paso como viene en el libro Python Crash Course

# Alien Colors # 1
# Crea una variable que almacene un color si este color al ejecutar la condición es True
# Imprimirá un mensaje que gano 5 puntos
# En este caso lo habrá salida si la condición es negativa

"""
AlienColor: str = 'Verde'
if AlienColor == 'Verde':
    print('Ganaste 5 puntos!')
"""

# Alien Colors # 2
# Ahora escribiremos una cadena if-elif para realizar una acción si es verdadera
# En este caso imagina que si le disparas al alien de color verde ganas 5 puntos
# y si le da al que sea rojo gana 10 puntos
# Aqui yo le puse la opción que puedas elegir el color para que se observe que
# sucede en cada salida.
# Si eliges un color que no esta en las opciones sale un mensaje

"""
InsertColor: str = input('\n *Verde \n *Rojo \n Elige un color: ')
if InsertColor == 'Verde':
    print('Ganaste 5 puntos!')
elif InsertColor == 'Rojo':
    print('Ganaste 10 puntos!')
"""

# Alien Colors # 3
# Ahora modificaremos un poco el paso anterior para generar una cadena if-elif-else
# Observanos que si elegimos el color amarillo entre en el else (FALSE).

"""
InsertColor: str = input('\n *Verde \n *Rojo \n *Amarillo \n Elige un color: ')
if InsertColor == 'Verde':
    print('Ganaste 5 puntos!')
elif InsertColor == 'Rojo':
    print('Ganaste 10 puntos!')
else:
    print('Ganaste 15 puntos!')
"""

# Stages of life
# En este ejemplo ahora veremos como delimitar en que periodo de su vida su encuentra una persona
# de acuerdo a diferentes rangos de edad

Edad: int = int(input('¿Cuantos años tiene el individuo?: '))
if Edad <= 2:
    print('Es un bébe.')
elif Edad <= 4:
    print('Es un niño pequeño.')
elif Edad <= 13:
    print('Es un niño.')
elif Edad <= 20:
    print('Es un adolescente.')
elif Edad < 65:
    print('Es un adulto.')
elif Edad >= 65:
    print('Es un anciano.')

# El programa de acuerdo al rango de edad te posiciona en la etapa que estas.

