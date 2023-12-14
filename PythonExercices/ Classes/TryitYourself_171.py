# TRY IT YOURSELF pag. 171 9-4 Number served
# Utiliza la clase del ejercicio 9-1 y agrega un atributo llamado number_served con un valor default 0

class Resturant():
    """Initialize restaurant_name and cuisine_type attributes"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        # ------------------------------------------ #
        # Valor default
        self.number_served = 0

    def describe_restaurant(self):
        print(f"El nombre del restaurante es: {self.restaurant_name.title()}")
        print(f"El tipo de cocina es: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(
            f"El restaurante: {self.restaurant_name.title()} esta abierto! y servirán comida: {self.cuisine_type.title()}")

    def set_number_served(self):
        """Este método cambia directamente el valor del atributo number_served()"""
        print(f"El numero de comensales servidos: {self.number_served}")

    def increment_number_served(self, served):
        """Añade la cantidad de nuevos comensales servidos"""
        self.number_served = self.number_served + served


# Crea una instancia a partir de la clase
restaurante1 = Resturant("El Chimichangas", "Mexicana")
numberOfClients = restaurante1.number_served = 50

# LLamar al método que imprime el valor actualizado
restaurante1.set_number_served()
# Message print: El numero de comensales servidos: 50

# LLamar al método increment_number_served()
restaurante1.increment_number_served(7)

# Llamar al método que imprime el valor de los comensales
restaurante1.set_number_served()
# Message print: El numero de comensales servidos: 57




