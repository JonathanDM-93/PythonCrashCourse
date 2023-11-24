class Dog:
    """A simple attempt to model dog"""

    def __init__(self, name, age):
        """Initialize name and attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")

    def rollover(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


# Creando una instancia que representa un perro
someDog = Dog("Terry", 5)
print(f"El nombre de mi perro es: {someDog.name.title()}.")
print(f"Mi perro tiene la edad de: {someDog.age}.")

someDog.sit()
someDog.rollover()

# El nombre de mi perro es: Terry.
# Mi perro tiene la edad de: 5.
# Terry is now sitting
# Terry rolled over!

