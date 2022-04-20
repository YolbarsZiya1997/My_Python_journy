class Car:
    """ A simple attempt to represent a car"""
    
    def __init__(self, make, model, year):   # Methodes
        """ Initialize attributes to describe a car"""
        self.make = make                # Attributes
        self.model = model
        self.year = year
        self.odometer_reading = 0       #default value for a car's mileage
        
        
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
    
my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23    #modifying attributes value directly
my_new_car.read_odometer()
print("*"*40)
# Modifying through a method
my_new_car.update_odometer(79)
my_new_car.read_odometer()
my_new_car.update_odometer(23)      #odometer cannot be rolled back
my_new_car.read_odometer()
print("#"*40)
my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)         #instances
my_used_car.read_odometer()
