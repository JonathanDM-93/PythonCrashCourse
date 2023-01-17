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

print('\n[*]\n')

# EJERCICIO 7-2 Restaurant Seating
# Crea un programa en donde se pregunte al usuario cuantas personas estaran en una cena
# si superan a más de ocho devolver un mensaje que deberan esperan una mesa pero si son
# menos de ocho decir que la mesa está disponible

print('\t Bienvenidos!')
dinner_people: int = int(input('- ¿Cuantas personas vienen a cenar? '))
if dinner_people >= 8:
    print('- Debera esperar un poco para su mesa.')
else:
    print('\n -Su mesa esta disponible. Pasen!')

# EJERCICIO 7-3 Multiples of ten
# Reporta si el número que ingresa un usuario es multiplo de 10.
# Aquí, use la analogía del número par solo que si al multiplicar por si mismo
# y al dividir entre 10 debe dar 0.

ten: int = int(input('Ingresa un número: '))
if ten*ten % 10 == 0:
    print('Es multiplo')
else:
    print('No es multiplo')
