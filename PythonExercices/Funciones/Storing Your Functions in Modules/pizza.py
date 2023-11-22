# Una de las ventajas de las funciones es la manera de separar en bloques de código tu código principal. Puedes almace-
# nar tus funciones en archivos separados llamados 'módulos' e importar estos módulos dentro de tu código principal.
# La declaración 'import' dice a Python hacer el código en un módulo disponible en el archivo de programa que se está
# ejecutando.

# Almacenar tus funciones en archivos separados permite tener ocultos los detalles del código de tu programa y enfocarte
# en la logica de alto nivel. También te pérmite reutilizar tus funciones en diferentes programas. Cuando almacenas
# tus funciones en archivos separados, tú puedes compartir estos archivos con otros programadores sin compartir tu
# programa entero. Conocer como importar estas funciones también te permite el uso de librerias o funciones que otros
# programadores han escrito.

# Para comenzar a importar funciones, comenzaremos a creando un módulo. Un módulo es un archivo con terminación .py que
# contiene el código que quieres importar dentro de tu programa. Creemos un módulo que contenga la función make_pizza()
# Para hacer este módulo que contiene este módulo, removeremos cualquier cosa del archivo pizza.py exepto la función
# make_pizza()

def make_pizza(size, *toppings):
    """Imprime la lista de toppings que han sido solicitados"""
    print(f"\n Cocinando una pizza de {str(size)} -pulgadas con los siguientes ingredientes: ")
    for topping in toppings:
        print("- " + topping)

