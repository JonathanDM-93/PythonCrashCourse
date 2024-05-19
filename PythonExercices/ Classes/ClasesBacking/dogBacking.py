class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


# Creemos una instancia que cree un perro.
# La clase Dog le dice a pyton como crear instancias/objetos individuales que representan a un perro en particular
my_dog = Dog(name="Drax", age=4)

# Imprimir un message usando las instancias
print("My dog´s name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
# My dog´s name is Drax.
# My dog is 4 years old.

# Aquí únicamente estoy llamando a las variables name & age que son llamadas "atributos" y como vemos solo toma
# la variable o atributo.

# Atributos
# Para acceder a los atributos de una instancia/objeto debes usar la notación [.]

# Llamando a los métodos/funciones
# Después de crear una instancia de la clase Dog, nosotros podemos usar la notación punto para llamar cualquier
# método definido en la clase Dog()

# Método sit()
my_dog.sit()