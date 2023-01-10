# Ahora bien ya vimos como hacer diccionarios, y anidar listas en diccionarios,
# veremos en este momento como anidar DICCIONARIOS DENTRO DE DICCIONARIOS.
# HERE WE GO!

usuarios: dict = {
    'Jonathan': {
        'Paterno': 'White',
        'Materno': 'Williams',
        'Locación': 'Atlanta',
    },
    'Ernesto': {
        'Paterno': 'McKenzie',
        'Materno': 'Turmelini',
        'Locación': 'Italia',
    },
}

for nombre, informacion in usuarios.items():
    print('\n' + 'NOMBRE: ' + nombre)
    print('\t' + 'NOMBRE COMPLETO: ' + informacion['Paterno'] + ' ' + informacion['Materno'])
    print('\t' + 'UBICACIÓN: ' + informacion['Locación'])



