class Car():
    """Initialize attributes to describe a car"""

    def __init__(self, make: str, model: str, year: str):
        self.make = make
        self.model = model
        self.year = year
        """Setting a Default Value for an Attribute"""
        self.odometer_reading = 0

    def get_describe_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + str(self.make) + ' ' + str(self.model)
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car´s mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("No puedes regresar el el kilometraje del odometer!")


# ------------------------------------------------------------------------------- #

# Crear la instancia/objeto
my_new_car = Car("Audi", "a4", "2016")

# Llamar al método/función
print(my_new_car.get_describe_name())

# LLamar al método/función read_odometer()
my_new_car.read_odometer()

# 1.-  *** Modificar el --atributo-- directamente ***
my_new_car.odometer_reading = 23

# Llamar al método/función
my_new_car.read_odometer()

# ------------------------------------------------------------------------------- #
print("\n[*]\n")

# Crear la instancia/objeto de un nuevo carro
secondCar = Car("Vento", "Starline", "2019")

# Llamar al método/función
print(secondCar.get_describe_name())

# LLamar al método que nos permite cambiar el valor del odometro
secondCar.update_odometer(5000)

secondCar.read_odometer()

# Modificar el kilometraje del odometer del objeto secondCar y generar la salida del else
secondCar.update_odometer(4999)
# No puedes regresar el el kilometraje del odometer!
# ------------------------------------------------------------------------------- #
print("\n[*]\n")
