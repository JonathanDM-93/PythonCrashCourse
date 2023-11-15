# TRY IT YOURSELF pag. 146 8-6 City Names
# Escribe una función llamada city_country() que tome el nombre de la ciudad y el país. La función debe retornar un
# string formateado como este # Santiago, Chile"

def city_country(enter_city, enter_country):
    address = f"{enter_city}, {enter_country}".title()
    return address


cityCountry: str = city_country("méxico", "cdmx")
# print(cityCountry)
# México, Cdmx


