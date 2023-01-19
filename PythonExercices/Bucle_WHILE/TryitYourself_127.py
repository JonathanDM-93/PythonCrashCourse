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

AgeInstructions: str = "\nPresiona 'q' para salir."
AgeInstructions += '\n¿Cual es tu edad: '

AsientosDisponibles: int = 5 # Variable que indica cuantos asientos están disponibles.
AgeMessage: str = "" # Mensaje vació que debe estar antes de comenzar el While.

#Crear el While con la condición que se terminara cuando el conteo sea igual a 0
while AsientosDisponibles != 0:
    AgeMessage = int(input(AgeInstructions)) # Se hizo un cast para convertir de str a int.
    AsientosDisponibles -= 1 # Se va reduciendo en 1 cada vez que se ocupe in asiento

    if AgeMessage <= 3:
        print('Tu entrada es gratis.')

    elif AgeMessage > 3 | AgeMessage < 12:
        print('Tu entrada cuesta $ 10.00')

    elif AgeMessage >= 12:
        print('Tu entrada cuesta $ 15.00')








