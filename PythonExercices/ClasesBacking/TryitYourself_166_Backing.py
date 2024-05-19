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

# someRestaurant.describe_restaurant()
# someRestaurant.open_restaurant()

# El nombre del restaurante es: El Italiano Loco
# El tipo de cocina es: Italiana
# El restaurante: El Italiano Loco esta abierto!


