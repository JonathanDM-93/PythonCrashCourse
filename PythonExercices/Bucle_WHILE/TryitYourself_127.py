# EJERCICIO 7-4 Hacer un programa donde el usuario ingrese sus ingredientes favoritos
# y se termine al ingresar quit.

pizzaIngredients: str = '\nAgrega los ingredientes que quieres en tu pizza: '
pizzaIngredients += '\nIngresa quit para finalizar tu orden. '

activeFlag: bool = True
ingredients: str = ""
while activeFlag:
    ingredients = input(pizzaIngredients)

    if ingredients == 'quit':
        activeFlag: bool = False
    else:
        print('El ingrediente que agregaste es: ' + ingredients)


# EJERCICIO 7-5 Movie tickets
# Modifica el programa para que se termine el loop

AgeInstructions: str = "\nPresiona 999 para salir."
AgeInstructions += '\n¿Cual es tu edad: '

AsientosDisponibles: int = 5 # Variable que indica cuantos asientos están disponibles.
AgeMessage: str = "" # Mensaje vació que debe estar antes de comenzar el While.

#Crear el While con la condición que se terminara cuando el conteo sea igual a 0
while AsientosDisponibles != 0:
    AgeMessage = input(AgeInstructions) # Se hizo un cast para convertir de str a int.
    Age_two : int = int(AgeMessage) # Se casteo nuevamente en otra variable para que no saliera error.
    AsientosDisponibles -= 1 # Se va reduciendo en 1 cada vez que se ocupe in asiento
    print ('* Asientos disponibles: ' + str(AsientosDisponibles))

    if Age_two == 999: # También si queremos que el programa se termine antes usamos break
        print('\n\t¡Hasta la vista baby!')
        break

    elif Age_two <= 3:
        print('Tu entrada es gratis.')

    elif Age_two in range(4,11):
        print('Tu entrada cuesta $ 10.00')

    elif Age_two >= 12:
        print('Tu entrada cuesta $ 15.00')








