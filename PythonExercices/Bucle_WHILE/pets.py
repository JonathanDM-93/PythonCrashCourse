# Removiendo todos los elementos de valores especificos de una lista.

# Creemos una lista con algunos elementos dentro.

VW_Models: list = ['Vento', 'Polo', 'Jetta', 'Tiguan', 'Polo', 'Polo']
# Listo!, ya tenemos nuestra lista ahora veremos como quitar ciertos elementos de la lista

while 'Polo' in VW_Models:
    VW_Models.remove('Polo')
    print(VW_Models)

# El while que está en la linea 8 dice esto: Mientras que 'Polo' este dentro de la lista VW_Models
# lo quitaras cada vez que lo encuentres
# Finalmente imprimes la lista.

# >> Cada ves que se recorre la lita se elimina el modelo que elegimos eliminar 'Polo'
# ['Vento', 'Jetta', 'Tiguan', 'Polo', 'Polo']
# ['Vento', 'Jetta', 'Tiguan', 'Polo']
# ['Vento', 'Jetta', 'Tiguan']