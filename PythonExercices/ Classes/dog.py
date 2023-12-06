class Dog:
    """A simple attempt to model dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")

    def rollover(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


# Creando una instancia que representa un perro
# Crear una variable, llamar a la clase y ingresar los argumentos.
someDog = Dog("Terry", 5)
print(f"El nombre de mi perro es: {someDog.name.title()}.")
print(f"Mi perro tiene la edad de: {someDog.age}.")

# Llama a la variable donde se almacenó la llamada de la clase y se llaman/acceden a las funciones dentro de la clase a
# traves del operador punto [.]
someDog.sit()
someDog.rollover()

# El nombre de mi perro es: Terry.
# Mi perro tiene la edad de: 5.
# Terry is now sitting
# Terry rolled over!

