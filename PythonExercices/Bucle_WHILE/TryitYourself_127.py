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

AgeUser: int = int(input('¿Cual es tu edad?: '))

if AgeUser < 3:
    print('Tu entrada es gratis.')
elif AgeUser > 3 | AgeUser < 12:
    print('Tu entrada cuesta $ 10.00')
elif AgeUser > 12:
    print('Tu entrada cuesta $ 15.00')







