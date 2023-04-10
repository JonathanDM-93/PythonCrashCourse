# Creación de las funciones

def twoparamas(one,two):
    if one >= two:
        print(str(one) + " es mayor.")
    if two >= one:
        print(str(two) + " es mayor")

if __name__ == "__main__":
    print("Ingresa dos valores: ")
    primervalor = int(input("Ingresa el primer valor: "))
    segundovalor = int(input("Ingresa el segundo valor: "))
    # Llamar a la función
    twoparamas(primervalor,segundovalor)