class Restaurant:
    """A class representing a restaurant"""

    def __init__(self, name, cuisine):
        """Initialize the restaurant"""
        self.name = name.title()
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Display a summary of the restaurant"""
        msg = f"{self.name} serves wonderful {self.cuisine}"
        print(f"\n{msg}")

    def open_restaurant(self):
        """Displays a message that the restaurant is opened"""
        msg = f"{self.name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number_served):
        """Allow user to set the number of customers that have been served"""
        self.number_served = number_served

    def increment_number_served(self, additional_served):
        """Allow user to increment the number of customers served."""
        self.number_served += additional_served


restaurant = Restaurant("Zafer", "Uighur")
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(1257)
print(f"Number served:{restaurant.number_served}")

restaurant.increment_number_served(131)
print(f"Number served: {restaurant.number_served}")
