# EJERCICIO 7-4
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


