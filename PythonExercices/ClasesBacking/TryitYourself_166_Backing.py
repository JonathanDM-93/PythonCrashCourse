# TRY IT YOURSELF pag. 166 9-1 Restaurant
# Crea una una clase llamada restaurante.

class Restaurant:
    def __init__(self, restaurant_name: str, cuisine_tpye: str):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_tpye

    """Definir los métodos"""

    def describe_restaurant(self):
        """Imprimirá dos mensajes"""
        print("El nombre del restaurante es: " + self.restaurant_name.title())
        print("El tipo de cocina es: " + self.cuisine_type.title())

    def open_restaurant(self):
        """Dira si el restaurante esta abierto"""
        print("El restaurante: " + self.restaurant_name.title() + " esta abierto!")


# Crear una instancia/objeto de la clase Restaurant()
someRestaurant = Restaurant("El italiano loco", "Italiana")

someRestaurant.describe_restaurant()
someRestaurant.open_restaurant()

# El nombre del restaurante es: El Italiano Loco
# El tipo de cocina es: Italiana
# El restaurante: El Italiano Loco está abierto!

print("\n[*]\n")

# TRY IT YOURSELF pag. 166 9-2 Three Restaurants
# Toma la clase anterior y crea tres diferentes instancias/objetos a partir de la clase y llama a describe_restaurant() para
# cada instancia.

mexicanRestaurant = Restaurant("El Mexicanito", "Mexicana")
mexicanRestaurant.describe_restaurant()
print("\n[-]\n")
ruskyRestaurant = Restaurant("El rusky bailarin", "Rusa")
ruskyRestaurant.describe_restaurant()
print("\n[-]\n")
japanRestaurant = Restaurant("El palillito feliz", "Japonea")
japanRestaurant.describe_restaurant()

print("\n[*]\n")


# TRY IT YOURSELF pag. 166 9-3 Users
# 1.- Crea una clase llamada User.
# 2.- Crea dos atributos first_name & last_name, y otros atributos que consideres que son típicamente usados al crear
# el perfil de un usuario
# 3.- Crea un método llamado describe_user() que imprima la información del usuario.
# 4.- Crea un segundo método llamado greet_user() que imprima un saludo personalizado para el usuario.


class User:
    """Initialize attributes"""

    def __init__(self, first_name: str, last_name: str, address: str, telephone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.telephone = telephone

    def greet_user(self):
        print(f"Mucho gusto: {self.first_name.title()} {self.last_name.title()} !")

    def describe_user(self):
        print(f"Esta es tu información:\n"
              f" [*] Nombre: {self.first_name.title()} \n"
              f" [*] Apellido: {self.last_name.title()} \n"
              f" [*] Dirección: {self.address.title()} \n"
              f" [*] Telefono: {self.telephone.title()}")


# Crear una instancia/objeto a partir de la clase
oneUser = User("Thomas", "Mackensee", "Lawrenceville, Georgia", "+441 362372888")

# Llamar al método/función greet_user() para mandar un saludo de bienvenida al usuario.
oneUser.greet_user()

# Llamar al método/función describe_user() la cual imprime la data del usuario.
oneUser.describe_user()
