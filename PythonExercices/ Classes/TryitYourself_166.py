# TRY IT YOURSELF pag. 166 9-1 Restaurant
# Crea una una clase llamada restaurante.

class Resturant:
    """Initialize restaurant_name and cuisine_type attributes"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"El nombre del restaurante es: {self.restaurant_name.title()}")
        print(f"El tipo de cocina es: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(
            f"El restaurante: {self.restaurant_name.title()} esta abierto! y servirán comida: {self.cuisine_type.title()}")


# Crear una instancia/objeto.
restaurant = Resturant("Los Locos Asados", "Asados")

# Llamar al la instancia/objeto y acceder a los atributos.
print(f"Mi restaurante favorito: {restaurant.restaurant_name}.")
print(f"Y su especialidad es: {restaurant.cuisine_type}")

# Acceder a los métodos/funciones de la clase.
restaurant.open_restaurant()

# Mi restaurante favorito: Los Locos Asados.
# Y su especialidad es: Asados
# El restaurante Los Locos Asados está abierto

print("\n[*]\n")

# TRY IT YOURSELF pag. 166 9-2 Three Restaurants
# Toma la clase anterior y crea tres diferentes instancias a partir de la clase y llama a describe_restaurant() para
# cada instancia.

# Crear instancias/objetos
restautantItalian = Resturant("Little Italy", "Italiana")
# Acceder a los métodos/funciones de la clase.
restautantItalian.describe_restaurant()

# Crear instancias/objetos
restaurantMexican = Resturant("El Grito de Guerra", "Mexicana")
# Acceder a los métodos/funciones de la clase.
restaurantMexican.describe_restaurant()

# Crear instancias/objetos
restaurantChinesse = Resturant("El ojos de regalo", "China")
# Acceder a los métodos/funciones de la clase.
restaurantChinesse.describe_restaurant()

# El nombre del restaurante es: Little Italy
# El tipo de cocina es: Italiana
# El nombre del restaurante es: El Grito De Guerra
# El tipo de cocina es: Mexicana
# El nombre del restaurante es: El Ojos De Regalo
# El tipo de cocina es: China

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

    def describe_user(self):
        print(f"Esta es tu información:\n"
              f" [*] Nombre: {self.first_name.title()} \n"
              f" [*] Apellido: {self.last_name.title()} \n"
              f" [*] Dirección: {self.address.title()} \n"
              f" [*] Telefono: {self.telephone.title()}")

    def greet_user(self):
        print(f"Mucho gusto: {self.first_name.title()} {self.last_name.title()} !")


# Crear una instancia/objeto a partir de la clase
oneUser = User("jonthan", "maldonado", "Lawrenceville, Georgia", "+441 362372888")

# Llamar al método/función greet_user() para mandar un saludo de bienvenida al usuario.
oneUser.greet_user()

# Llamar al método/función describe_user() la cual imprime la data del usuario.
oneUser.describe_user()
