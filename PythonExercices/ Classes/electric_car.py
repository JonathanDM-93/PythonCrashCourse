class Car:
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
            print("You can´t roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


# El nombre de la clase padre debe ir dentro de los parentesis en la definición de la clase hija.
class ElectricCar(Car):
    def __init__(self, make: str, model: str, year: str):
        """Connection between parent class and child class"""
        super().__init__(make, model, year)


# ----------------------------------------------------------- #

# Crear una instancia/objeto
myToyota = ElectricCar("Toyota", "Yaris", "2023")

# Llamar al método/función de la parent class
print(myToyota.get_describe_name())
