class Restaurant:
    """ A simple attempt to model a restaurant."""
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
            print(f"The name of this restaurant is {self.name}")
            print(f"It serves {self.cuisine_type} cuisine")
            
            
    def set_number_served(self, servings):
            self.number_served = servings
    
    def service_reader(self):
        print(f"Number of service is {self.number_served}")
                
    def increment_number_served(self, plates):
            self.number_served += plates

class IceCreamStand(Restaurant):
    """ MacFlurry machine is broken again come to the rescue"""
    def __init__(self, name, cuisine_type='ice_cream'):
        """ Initialize the attributes for the parent class"""
        super().__init__(name, cuisine_type)
        self.flavors = []
        
    def show_flavors(self):
        """Show all flavors of ice creams"""
        print(f"\nThe types of flavors are as follow: ")
        for flavor in self.flavors:
            print(f"- {flavor}")
        
        
big_one         = IceCreamStand("The big one")
big_one.flavors = ["vanilla", "chocolate", "black cherry"]
big_one.show_flavors()