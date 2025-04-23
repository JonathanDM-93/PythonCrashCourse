class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make: str, model: str, year: int):
        """Initialize the car's attributes."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car´s mileage"""
        print("The car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage: int):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can´t roll back an odometer!")

    def increment_odometer(self, miles: int):
        self.odometer_reading += miles


# Crear una instancia/objeto a partir de la clase
my_new_car = Car("Vento", "Starline", 2019)
print(my_new_car.get_descriptive_name())
# 2019 Vento Starline

print("\n[-]\n")

# Cambiar el valor del odómetro
my_new_car.update_odometer(23500)
my_new_car.read_odometer()
# The car has 23500 miles on it.
# - Llame a la instancia con el otro método de incremento y vi el cambio
my_new_car.increment_odometer(100)
my_new_car.read_odometer()
# The car has 23600 mil es on it.
