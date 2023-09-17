# TRY IT YOURSELF pag. 135 8-1 Message
# Escribir una función basic que imprima un mensaje

def message():
    print("Declaración de funciones!")


# TRY IT YOURSELF pag. 135 8-2 Favorite Book
# Declarar la función aquí
def book(libro):
    print(f"Este es tu libro favorito: {libro} ")


# Ejecución del script
if __name__ == "__main__":

    # LLamar a la función message
    message()

    # Llamar a la función book
    favorite_book = str(input("¿Cuál es tu libro favorito?"))
    book(favorite_book)
