class Restaurant:
    """ Describe a restaurant""" 
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """ Describe the restaurant"""
        description = f"{self.name} serves wonderful {self.cuisine_type} cuisine"
        print(f"{description}")
        
    def open_restaurant(self):
        """ Invites the guests in"""
        invitation = f"{self.name} is opened, come on in"
        print(f'{invitation}')
        
    
restaurant = Restaurant('Zafer', 'Uighur')
restaurant.open_restaurant()
restaurant.describe_restaurant()
