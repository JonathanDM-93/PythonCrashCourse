# TRY IT YOURSELF pag. 166 9-1 Restaurant
# Crea una una clase llamada restaurante.

class Resturant():
    """Initialize restaurant_name and cuisine_type attributes"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"El nombre del restaurante es: {self.restaurant_name.title()}")
        print(f"El tipo de cocina es: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"El restaurante {self.restaurant_name.title()} esta abierto!")


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


