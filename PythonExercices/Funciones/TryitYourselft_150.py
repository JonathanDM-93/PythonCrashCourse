# TRY IT YOURSELF pag. 150 8-9 Magicians
# Crea una lista de nombres de magos. Pasa la lista a una función llamada show_magicians(), la cual imprima
# el nombre de cada mago en la lista.

def show_magicians(enter_mags):
    for names in enter_mags:
        print(f"{names}")


# Crea una lista con nombres de magos
namesOfMagicians: list = ['Gandalf', 'Saruman', 'Harry Potter']

# Llama a la función
show_magicians(namesOfMagicians)

# Gandalf
# Saruman
# Harry Potter

print('\n[*]\n')


# TRY IT YOURSELF pag. 150 8-10 Great Magicians
# Empieza con una copia de la anterior función del ejercicio anterior, pero crea otra función llamada make_great() que
# modifique la lista de los magos agregando la frase 'Great' en cada nombre del mago. Llama a show_magicians() para ver
# como se ve la lista modificada.

# Recibe la lista de los magos
def make_great(magiciansNames):
    for names in magiciansNames:
        print(f"Great {names}")


# Crea una lista de magos
otherMagicians: list = ['Dr. Strage', 'Morgana', 'Voldemort']

# Llamar a las funciones
make_great(otherMagicians)
show_magicians(otherMagicians)

print('\n[*]\n')


