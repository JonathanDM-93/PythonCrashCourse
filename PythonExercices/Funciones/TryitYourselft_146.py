# TRY IT YOURSELF pag. 146 8-6 City Names
# Escribe una función llamada city_country() que tome el nombre de la ciudad y el país. La función debe retornar un
# string formateado como este # Santiago, Chile"

def city_country(enter_city, enter_country):
    address = f"{enter_city}, {enter_country}".title()
    return address


cityCountry: str = city_country("méxico", "cdmx")


# print(cityCountry)
# México, Cdmx

# TRY IT YOURSELF pag. 146 8-7 Album
def make_album(nameArtist, albumTitle, numsTraks=''):
    disco: dict = {'name': nameArtist,
                   'album': albumTitle, }
    if numsTraks:
        disco['canciones'] = numsTraks
    return disco


# Declarar un contador
contador = 0
# Declarar un límite de entradas
limitDict = 2

# Solo permite el ingreso de tres diccionarios
while contador <= limitDict:
    ingresaArtista = input("Ingresa el nombre del Artista: ")
    ingresaAlbum = input("Ingresa nombre del Albúm: ")
    ingresaCanciones = input("Ingresa el número canciones: ")

    # Aunque el límite es de 3 Artistas, puedes terminar antes sio ingresas 'no'
    terminarAntes = input("¿Quieres agregar otro Artista? (si/no) ")
    if terminarAntes == 'no':
        break

    # O puedes continuar ingresando hasta llegar al limite de 3
    elif terminarAntes == 'si':
        artistAlbum = make_album(ingresaArtista, ingresaAlbum, ingresaCanciones)
        print(artistAlbum)
        contador += 1
