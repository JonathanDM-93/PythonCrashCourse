# Para salir inmediatamente de un loop While sin ejecutar el correo remanente
# podemos usar la declaración BREAK. Esta nos permite dirigir el flujo de un programa
# Vemos un ejemplo

placesVisited: str = '\nPor favor ingresa los lugares que haz visitado: '
placesVisited += '\nIngresa quit para salir del programa. '

while True:  # El inicio del loop inicia como TRUE y preguntara siempre hasta que se ingrese quit
    city = input(placesVisited)  # La variable message recibirá lo que el usuario ingreso
    if city == 'quit':  # Si la palabra es quit se termina el programa
        break
    else:
        print('Me encanto ' + city.title() + '!') # Si la condición es FALSA A AL SER NEGATIVA sigue el programa.