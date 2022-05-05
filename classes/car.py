class Car:
    """ A simple attempt to represent a car"""

    def __init__(self, make, model, year):  # Methods
        """ Initialize attributes to describe a car"""
        self.make = make  # Attributes
        self.model = model
        self.year = year
        self.odometer_reading = 0  # default value for a car's mileage

    def get_descriptive_name(self):
        """ Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def upgrade_battery(self):
        print(f"Current battery size... {self.battery_size}")
        if self.battery_size < 100:
            print("Upgrade needed...")
            print("Upgrading...")
            self.battery_size = 100
            print(f"Upgrade complete. Current battery size is {self.battery_size}")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            ranges = 260
        elif self.battery_size == 100:
            ranges = 315

        print(f"This car can go about {ranges} miles on a full charge.")

class ElectricCar(Car):  # The child class
    """ Represent aspect of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
            Then initialize attributes specific to an electric car."""

        super().__init__(make, model, year)
        self.battery = Battery()

    @staticmethod
    def fill_gas_tank():
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")  # Overriding Methods from the parent class

# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.read_odometer()
# my_new_car.odometer_reading = 23  # modifying attributes value directly
# my_new_car.read_odometer()
# print("*" * 40)
# # Modifying through a method
# my_new_car.update_odometer(79)
# my_new_car.read_odometer()
# my_new_car.update_odometer(23)  # odometer cannot be rolled back
# my_new_car.read_odometer()
# print("#" * 40)
# my_used_car = Car('subaru', 'outback', 2015)
# print(my_used_car.get_descriptive_name())
#
# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()
#
# my_used_car.increment_odometer(100)  # instances
# my_used_car.read_odometer()
