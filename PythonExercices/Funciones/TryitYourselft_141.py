# TRY IT YOURSELF pag. 135 8-3 T-Shirt
# Escribir una función llamada make_shirt() que acepte el tamaño y devuelva un mensaje
# Llama la función con posicion de argumento y después con argumento keyword

def make_shirt(texto_mensaje, talla, ):
    # El tamaño de la camisa es:
    print(f"{texto_mensaje} {talla} ")


# Llamar a la función con argumentos de posición
# Esta, padre que el editor de texto lo asigne como si fueran argumentos keyword
make_shirt("El tamaño de la camisa es:", "chica")
# El tamaño de la camisa es:  chica

print("\n")

# Declarar las variables
texto: str = "La camisa es pequeña, porque la talla es:"
camisa_talla: str = "Mediana"

# Llamar a la función con argumentos keywords
make_shirt(texto_mensaje=texto, talla=camisa_talla)


# TRY IT YOURSELF pag. 141 8-4 Large Shirts
# Modifica la función make_shirt() donde el tamaño de las camisas sean largas por default más un mensaje que diga
# "I love Python"
# Crearé una función algo más compleja.


def custom_shirt():
    bandera = True
    while bandera:
        tallaCamisa = input("¿Qué tamaño de camiseta necesitas? : ")
        mensajeCamisa = input("¿Qué mensaje deseas que tenga tu camisa? : ")

        if tallaCamisa == "Pequeña":
            if len(mensajeCamisa) <= 15:
                print(f"La camisa seleccionada es: {tallaCamisa} y el mensaje será: {mensajeCamisa}")
                bandera = False
            else:
                respuesta = input(
                    "El mensaje es demasiado largo, elige otro tamaño de camisa. ¿Quieres elegir otro tamaño? (si/no): ")
                if respuesta == "si":
                    bandera = True

        elif tallaCamisa == "Mediana":
            if 20 <= len(mensajeCamisa) <= 25:
                print(f"La camisa seleccionada es: {tallaCamisa} y el mensaje será: {mensajeCamisa}")
            else:
                respuesta = input(
                    "El mensaje es demasiado largo, elige otro tamaño de camisa. ¿Quieres elegir otro tamaño? (si/no): ")
                if respuesta == "si":
                    bandera = True

        elif tallaCamisa == "Grande":
            if 30 < len(mensajeCamisa) < 35:
                print(f"La camisa seleccionada es: {tallaCamisa} y el mensaje será: {mensajeCamisa}")
                bandera = False
            else:
                print("Lo sentimos no podemos agregar mensajes mas largos")
                break


# Llamar a la función
custom_shirt()
