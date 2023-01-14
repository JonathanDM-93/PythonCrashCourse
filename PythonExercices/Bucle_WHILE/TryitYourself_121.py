# EJERCICIO 7-1
car: str = input('¿Qué tipo de carro quieres rentar? ')
Active_cars: dict = {
    'cars': ['Vento', 'Impala', 'Mazda 3', 'Malibu'],
}

# Checar si el auto que quiere el cliente está en la lista o preguntarle si quiere otra opción
for modelos in Active_cars['cars']:
    if car == modelos:
        print('Si tenemos disponible:')
    else:
        print('No tenemos el auto que buscas. ¿Quieres que te muestre otro auto?')
