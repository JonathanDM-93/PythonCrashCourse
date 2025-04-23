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

print("\n[*]\n")


# Message print: El numero de comensales servidos: 57

# TRY IT YOURSELF pag. 171 9-5 Login Attempts.
# Agrega un atributo llamado login_attempts a la clase User de la pag.
# 166. Escribe un método llamado increment_login_attempts() que incremente el valor de login_attempts por 1. Escribe
# otro método llamado reset_login_attempts() que reinicie el valor a 0 Crea una instancia de la clase User y llama a
# increment_login_attempts() varias veces. Imprime el valor de login_attempts para verificar que se incrementa. Llama
# a reset_login_attempts() y verifica que el valor de login_attempts se reinicia a 0

class User:
    """Initialize attributes"""

    def __init__(self, first_name: str, last_name: str, address: str, telephone: str):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.telephone = telephone

        # ------------------------------------------ #
        # Agregar un atributo login_attempts
        self.login_attempts = 0
        # ------------------------------------------ #

    def increment_login_attempts(self, other_client: int):
        self.login_attempts += other_client

    def reset_login_attempts(self):
        """Reinicia el valor de login_attempts a 0"""
        self.login_attempts = 0

    def read_clients(self):
        print(f"El número de clientes: {self.login_attempts}")


new_user = User("John", "Malcovich", "Calle 123", "555-1234")
new_user.increment_login_attempts(15)
new_user.read_clients()

# Resetear el valor de login_attempts
new_user.reset_login_attempts()
new_user.read_clients()